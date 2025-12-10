import sqlite3

conn = sqlite3.connect("ecom.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    product_name TEXT,
    quantity INTEGER,
    price REAL,
    total_amount REAL,
    order_date TEXT,
    channel TEXT
);
""")

sample_data = [
    ("Arun", "T-Shirt", 2, 299, 598, "2025-01-01", "Whatsapp"),
    ("Vicky", "T-Shirt", 1, 299, 299, "2025-01-02", "Amazon"),
    ("Kumar", "Hoodie", 1, 799, 799, "2025-01-03", "Meesho")
]

cur.executemany("""
INSERT INTO orders (customer_name, product_name, quantity, price, total_amount, order_date, channel)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", sample_data)

conn.commit()
conn.close()

print("✔ Database created successfully with sample data!")
import sqlite3

conn = sqlite3.connect("ecom.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    product_name TEXT,
    quantity INTEGER,
    price REAL,
    total_amount REAL,
    order_date TEXT,
    channel TEXT
);
""")

# sample data
cur.execute("""
INSERT INTO orders (customer_name, product_name, quantity, price, total_amount, order_date, channel)
VALUES
('Arun', 'T-Shirt', 2, 299, 598, '2025-01-01', 'Whatsapp'),
('Vicky', 'T-Shirt', 1, 299, 299, '2025-01-02', 'Amazon'),
('Kumar', 'Hoodie', 1, 799, 799, '2025-01-03', 'Meesho');
""")

conn.commit()
conn.close()

print("Database created + sample data added.")
