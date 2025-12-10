-- SQLite schema for E-Commerce T-Shirt project
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    name TEXT,
    size TEXT,
    color TEXT,
    category TEXT,
    cost_price REAL,
    selling_price REAL
);

CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    phone TEXT,
    location TEXT
);

CREATE TABLE IF NOT EXISTS sales_channels (
    channel_id INTEGER PRIMARY KEY,
    channel_name TEXT
);

CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    order_date TEXT,
    customer_id INTEGER,
    channel_id INTEGER,
    total_amount REAL,
    payment_method TEXT,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY(channel_id) REFERENCES sales_channels(channel_id)
);

CREATE TABLE IF NOT EXISTS order_items (
    order_item_id INTEGER PRIMARY KEY,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    price REAL,
    FOREIGN KEY(order_id) REFERENCES orders(order_id),
    FOREIGN KEY(product_id) REFERENCES products(product_id)
);
