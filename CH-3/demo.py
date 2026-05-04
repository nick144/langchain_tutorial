import sqlite3

conn = sqlite3.connect("sales_db/sales.db")
cursor = conn.cursor()

# with cursor as cursor:
cursor.execute("SELECT * FROM orders")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()