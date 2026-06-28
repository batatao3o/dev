import json

class Customer:
    def __init__(self, name, email, balance):
        self.name = name
        self.email = email
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'{self.name} deposited {amount} euros. new balance: {self.balance} euros')

    def withdraw(self, amount):
        if amount > self.balance:
            print(f'{self.name} has insufficient funds. current balance: {self.balance} euros')
        else:
            self.balance -= amount
            print(f'{self.name} withdrew {amount} euros. new balance: {self.balance} euros')


    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'balance': self.balance
        }
    
    def show(self):
        print(f'--- {self.name} ---')
        print(f'email: {self.email}')
        print(f'balance: {self.balance} euros')
    
berat  = Customer('Berat',  'berat@email.com',  150)
jordan = Customer('Jordan', 'jordan@email.com', 350)
pasa = Customer('Pasa', 'pasa@email.com', 200.000)


# Make some transactions
berat.deposit(300)
jordan.deposit(100)
berat.withdraw(102)
jordan.withdraw(500)
pasa.deposit(670)
pasa.withdraw(100)



customers = [berat.to_dict(), jordan.to_dict(), pasa.to_dict()]
with open('customers.json', 'w') as file:
    json.dump(customers, file, indent=4)

print('customers saved')

with open('customers.json', 'r') as file:
    loaded = json.load(file)

for c in loaded:
    print(f"{c['name']} has {c['balance']} euros")

