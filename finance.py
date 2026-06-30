import json

class Transaction:
    def __init__(self, type, amount, description):
        self.type = type          # 'income' or 'expense'
        self.amount = amount      # the number eg 500
        self.description = description  # eg 'freelance job'
    
    def to_dict(self):
        return{
        'type' : self.type,
        'amount' : self.amount,
        'description' : self.description,
        }

class Tracker:
    def __init__(self):
        self.transactions = []

    def add_income(self, amount, description):
        transaction = Transaction('income', amount, description)
        self.transactions.append(transaction)

    def add_expense(self, amount, description):
        transaction = Transaction('expense', amount, description)
        self.transactions.append(transaction)
    
    def show_summary(self):
        balance = 0
        for transaction in self.transactions:
            print(f'{transaction.type} {transaction.amount} {transaction.description}')
            
        for transaction in self.transactions:
            if transaction.type == 'income':
                balance += transaction.amount
            else:
                balance -= transaction.amount
        print(f'total balance: {balance}')

    def save(self):
        data = []
        for transaction in self.transactions:
            data.append(transaction.to_dict())
        with open('finance.json', 'w') as file:
            json.dump(data, file, indent=4)
    def load(self):
        try:
            with open('finance.json', 'r') as file:
                data = json.load(file)
            for item in data:
                transaction = Transaction(item['type'], item['amount'], item['description'])
                self.transactions.append(transaction)
        except FileNotFoundError:
            pass


tracker = Tracker()
tracker.load()

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
        tracker.add_income(int(amount), description)
        tracker.save()
    elif choice == '2':
        amount = input('enter expense:')
        description = input('enter descrioption:')
        tracker.add_expense(int(amount), description)
        tracker.save()
    elif choice == '3':
        tracker.show_summary()
    else: 
        print('Goodbye!')
        break
    





        
