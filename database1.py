import sqlite3

conn = sqlite3.connect("webd.db")
c = conn.cursor()

c.execute("""
      CREATE TABLE IF NOT EXISTS website (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      username TEXT NOT NULL,
      email TEXT NOT NULL,
      password TEXT NOT NULL
      )
  """)
c.execute("""
      CREATE TABLE IF NOT EXISTS contacts (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      email TEXT NOT NULL,
      comment TEXT NOT NULL
      )
  """)
c.execute("""
DELETE FROM contacts
""")
conn.commit()

conn.close()