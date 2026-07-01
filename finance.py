import sqlite3

class Tracker:
    def __init__(self):
        self.conn = sqlite3.connect('finance.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                type TEXT,
                amount REAL,
                description TEXT
        )
        ''')
        self.conn.commit()

    def add_income(self, amount, description):
        self.cursor.execute('''
            INSERT into transactions (type, amount, description)
            VALUES (?, ?, ?)
        ''', ('income', amount,description))
        self.conn.commit()

    def add_expense(self, amount, description):
        self.cursor.execute('''
            INSERT into transactions (type, amount, description)
            VALUES (?, ?, ?)
        ''', ('expense', amount, description))
        self.conn.commit()
    
    def show_summary(self):
        self.cursor.execute('SELECT * FROM transactions')
        rows = self.cursor.fetchall()
        balance = 0
        for row in rows:
            print(f'{row[1]} {row[2]} {row[3]}')
            if row[1] == 'income':
                balance += row[2]
            else:
                balance -= row[2]

        print(f'total balance: {balance}')



tracker = Tracker()


while True:
    print('what do you want to do?')
    print('1. add income')
    print('2. add expense')
    print('3. show summary')
    print('4. quit')

    choice = input()
    if choice == '1':
        amount = input('enter amount:')
        description = input('enter description:')
        try:
            tracker.add_income(int(amount), description)
        except ValueError:
            print('That is not an amount')
    elif choice == '2':
        amount = input('enter expense:')
        description = input('enter descrioption:')
        try:
            tracker.add_expense(int(amount), description)
        except ValueError:
            print('That is not an amount')
    elif choice == '3':
        tracker.show_summary()
    else: 
        print('Goodbye!')
        break
