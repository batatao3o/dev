import sqlite3

# connect to database (creates file if it doesn't exist)
conn = sqlite3.connect('mydata.db')
cursor = conn.cursor()

# create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY,
        type TEXT,
        amount REAL,
        description TEXT
    )
''')

conn.commit()
print('database ready')
# insert a transaction
cursor.execute('''
    INSERT INTO transactions (type, amount, description)
    VALUES (?, ?, ?)
''', ('income', 500, 'freelance job'))

conn.commit()
print('data saved')
# get all transactions
cursor.execute('SELECT * FROM transactions')
rows = cursor.fetchall()

for row in rows:
    print(row)
conn.close()