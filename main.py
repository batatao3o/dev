from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    conn = sqlite3.connect('finance.db')
    return conn

class Transaction(BaseModel):
    type: str
    amount: float
    description: str

@app.get('/')
def home():
    return {'message': 'Finance Tracker API is running'}

@app.post('/add')
def add_transaction(transaction: Transaction):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO transactions (type, amount, description)
        VALUES (?, ?, ?)
    ''', (transaction.type, transaction.amount, transaction.description))
    conn.commit()
    conn.close()
    return {'message': 'transaction saved'}

@app.get('/summary')
def get_summary():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM transactions')
    rows = cursor.fetchall()
    conn.close()
    transactions = []
    balance = 0
    for row in rows:
        transactions.append({
            'type': row[1],
            'amount': row[2],
            'description': row[3]
        })
        if row[1] == 'income':
            balance += row[2]
        else:
            balance -= row[2]
    return {'transactions': transactions, 'balance': balance}