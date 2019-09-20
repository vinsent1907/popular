import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

sql = "SELECT * FROM albums WHERE artist=?"
cursor.execute(sql, [("RED")])
print(cursor.fetchall())