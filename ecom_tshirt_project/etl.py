import pandas as pd
import sqlite3
from pathlib import Path

DATA_DIR = Path("data")
DB_PATH = Path("tshirt.db")

def load_csv(name):
    return pd.read_csv(DATA_DIR / name)

def create_db():
    conn = sqlite3.connect(DB_PATH)
    with open("schema.sql", "r") as f:
        sql = f.read()
    conn.executescript(sql)
    conn.commit()
    conn.close()

def insert_table(df, table_name, conn):
    df.to_sql(table_name, conn, if_exists="append", index=False)

def run_etl():
    create_db()
    conn = sqlite3.connect(DB_PATH)
    # Load master/reference tables
    products = load_csv("products.csv")
    customers = load_csv("customers.csv")
    channels = load_csv("sales_channels.csv")
    insert_table(products, "products", conn)
    insert_table(customers, "customers", conn)
    insert_table(channels, "sales_channels", conn)

    # Load sales data (three sample files)
    for fname, table_orders, table_items in [
        ("amazon_sales.csv", "orders", "order_items"),
        ("whatsapp_orders.csv", "orders", "order_items"),
        ("daily_bills.csv", "orders", "order_items"),
    ]:
        df = load_csv(fname)
        # Normalize column names expected by schema
        # orders columns: order_id, order_date, customer_id, channel_id, total_amount, payment_method
        # order_items columns: order_item_id, order_id, product_id, quantity, price
        orders_cols = ["order_id","order_date","customer_id","channel_id","total_amount","payment_method"]
        items_cols = ["order_item_id","order_id","product_id","quantity","price"]
        orders = df[orders_cols].drop_duplicates(subset=["order_id"])
        items = df[items_cols]
        insert_table(orders, "orders", conn)
        insert_table(items, "order_items", conn)

    conn.commit()

    # Sample analytics queries
    print("\n=== SAMPLE ANALYTICS ===\n")
    q1 = "SELECT SUM(total_amount) FROM orders;"
    print('Total sales:', conn.execute(q1).fetchone()[0])

    q2 = "SELECT s.channel_name, SUM(o.total_amount) FROM orders o JOIN sales_channels s ON o.channel_id = s.channel_id GROUP BY s.channel_name;"
    print('\nSales by channel:\n', conn.execute(q2).fetchall())

    q3 = "SELECT p.name, SUM(oi.quantity) AS qty FROM order_items oi JOIN products p ON oi.product_id = p.product_id GROUP BY p.name ORDER BY qty DESC LIMIT 5;"
    print('\nTop products:\n', conn.execute(q3).fetchall())

    conn.close()

if __name__ == '__main__':
    run_etl()
