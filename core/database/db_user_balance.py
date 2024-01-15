import sqlite3 as sq

db = sq.connect('aiogram2.db')
cur = db.cursor()


def create_user_id_and_balance(user_id):
    cur.execute('''CREATE TABLE IF NOT EXISTS user_balance (
    id INTEGER PRIMARY KEY,
    balance INTEGER
    )''')
    db.commit()

    cur.execute('''SELECT id FROM user_balance WHERE id = ?''', (user_id,))
    existing_user = cur.fetchone()
    if existing_user is None:
        cur.execute('''INSERT INTO user_balance (id, balance) VALUES (?, ?)''', (user_id, 0,))
        db.commit()


def display_balance(user_id):
    cur.execute("SELECT balance, id FROM user_balance WHERE id = ?", (user_id,))
    entry = cur.fetchone()
    return entry


def add_balance(user_id, amount):
    cur.execute("UPDATE user_balance SET balance = balance + ? WHERE id = ?", (amount, user_id))
    db.commit()


def subtract_balance(user_id: int, amount: int):
    cur.execute("UPDATE user_balance SET balance = balance - ? WHERE id = ? AND balance >= ?",
                (amount, user_id, amount))
    affected_rows = cur.rowcount
    db.commit()

    if affected_rows == 0:
        return False
    else:
        return True
