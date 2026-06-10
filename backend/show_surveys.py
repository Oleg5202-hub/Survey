import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

cursor.execute("SELECT * FROM survey")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
