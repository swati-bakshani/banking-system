import sqlite3

def connect_db():
    conn = sqlite3.connect('bankingsystem.db')
    print('connected successfully')
    return conn

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE table IF NOT EXISTS accounts(
            account_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            balance REAL NOT NULL DEFAULT 0.0
        )
    ''')
    conn.commit()
    conn.close()

def create_account(name, initial_balance = 0.0):
    conn  = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT into accounts (name,balance) VALUES (?,?)", (name,initial_balance)
    )
    conn.commit()
    print("Account created Successfully")
    conn.close()

def deposit_amount(account_id,amount):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE accounts SET balance = balance + ? WHERE account_id = ?", (amount,account_id)
    )
    conn.commit()
    print("Deposited Successfully!")
    conn.close()

def withdrawl_amount(account_id,amount):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT balance FROM accounts WHERE account_id = ?", (account_id)
    )
    balance =cursor.fetchone()[0]
    print(f"your current balance is : INR {balance}")

    if balance >= amount:
        cursor.execute(
            "UPDATE accounts SET balance = balance - ? WHERE account_id = ?", (amount,account_id)
        )
        conn.commit()
        print("Withdrawal Successfully!")
    else:
        print("Insuficient Balance")

    conn.close()

def check_balance(account_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT balance FROM accounts WHERE account_id = ?", (account_id,)
    )
    balance = cursor.fetchone()[0]
    # print(cursor.fetchone())
    # conn.commit()
    print(f"your current balance is : INR {balance}")
    conn.close()




if __name__ == '__main__':
    connect_db()
    create_table()
    # create_account("john", 5000)
    # create_account("nikhil", 100000)
    # deposit_amount(2,5000)
    check_balance(2)
