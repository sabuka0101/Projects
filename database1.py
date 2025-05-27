import sqlite3

conn = sqlite3.connect("webd.db")
c = conn.cursor()

# Create tables
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

c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        author TEXT NOT NULL
    )
''')

# Add column operation
try:
    conn.execute("ALTER TABLE posts ADD COLUMN short_description TEXT NOT NULL DEFAULT ''")
except sqlite3.OperationalError:
    pass  # Column may already exist

# Create user
conn.execute('''
    INSERT INTO users (username, email, password) VALUES (?, ?, ?)
''', ('saba', 'sabachxo@gmail.com', '12341234'))

# Delete operation
conn.execute('''
    DELETE FROM users WHERE id = 1
''')

# Read operation
c.execute('SELECT id, username FROM users')
rows = c.fetchall()
for row in rows:
    print(f"ID: {row[0]}, Username: {row[1]}")

conn.commit()
conn.close()
