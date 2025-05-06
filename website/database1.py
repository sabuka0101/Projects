import sqlite3

conn = sqlite3.connect("webd.db")
c = conn.cursor()

c.execute("""
      CREATE TABLE IF NOT EXISTS website (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      username TEXT NOT NULL,
      email TEXT NOT NULL,
      age INTEGER NOT NULL
      )
  """)

conn.commit()

conn.close()