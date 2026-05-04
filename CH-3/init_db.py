import sqlite3
import os

os.makedirs("sales_db", exist_ok=True)

conn = sqlite3.connect("sales_db/sales.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT NOT NULL,
        product_name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL,
        total REAL NOT NULL,
        sale_date TEXT NOT NULL
    )
""")

cursor.execute("""
    INSERT INTO orders (
        customer_name,
        product_name,
        quantity,
        price,
        total,
        sale_date
    )
    VALUES 
    ('Alice', 'Laptop', 1, 999.99, 999.99, '2024-01-15'),
    ('Bob', 'Smartphone', 2, 499.99, 999.98, '2024-01-16'),
    ('Charlie', 'Headphones', 3, 199.99, 599.97, '2024-01-17'),
    ('David', 'Monitor', 1, 299.99, 299.99, '2024-01-18'),
    ('Eve', 'Keyboard', 2, 89.99, 179.98, '2024-01-19')
""")

conn.commit()
conn.close()