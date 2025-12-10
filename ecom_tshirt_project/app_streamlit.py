import streamlit as st
import pandas as pd
import sqlite3
from pathlib import Path
import matplotlib.pyplot as plt

DB_PATH = Path("tshirt.db")

@st.cache_data
def load_table(query):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

st.title("E-Commerce T-Shirt Dashboard")

# Key metrics
total_sales = load_table("SELECT SUM(total_amount) as total FROM orders;")['total'].iloc[0]
st.metric("Total Sales", f"₹{total_sales:,.2f}")

sales_by_channel = load_table("SELECT s.channel_name, SUM(o.total_amount) as amt FROM orders o JOIN sales_channels s ON o.channel_id = s.channel_id GROUP BY s.channel_name;")
st.subheader("Sales by Channel")
st.table(sales_by_channel)

st.subheader("Top Products by Quantity Sold")
top_products = load_table("SELECT p.name, SUM(oi.quantity) as qty FROM order_items oi JOIN products p ON oi.product_id = p.product_id GROUP BY p.name ORDER BY qty DESC LIMIT 10;")
st.table(top_products)

st.subheader("Daily Sales Trend")
daily = load_table("SELECT order_date, SUM(total_amount) as amt FROM orders GROUP BY order_date ORDER BY order_date;")
if not daily.empty:
    fig, ax = plt.subplots()
    ax.plot(pd.to_datetime(daily['order_date']), daily['amt'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    st.pyplot(fig)

st.subheader("Orders (preview)")
orders_preview = load_table("SELECT * FROM orders ORDER BY order_date DESC LIMIT 50;")
st.dataframe(orders_preview)
