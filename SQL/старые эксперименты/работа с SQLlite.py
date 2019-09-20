import sqlite3
import sys

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# создание таблицы
#cursor.execute("""CREATE TABLE albums
#                  (title text, artist text)
#               """)

# Вставляем данные в таблицу
cursor.execute("""INSERT INTO albums
                  VALUES ('Glow', 'Andy Hunter')"""
               )
# Вставляем множество данных в таблицу используя безопасный метод "?"
albums = [('Exodus', 'Andy Hunter'),
          ('Until We Have Faces', 'Red'),
          ('The End is Where We Begin', 'Thousand Foot Krutch'),
          ('The Good Life', 'Trip Lee')]
cursor.executemany("INSERT INTO albums VALUES (?,?)", albums)
conn.commit()
conn.close()