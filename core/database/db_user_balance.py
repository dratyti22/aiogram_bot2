import sqlite3 as sq

db = sq.connect('aiogram2.db')
cur = db.cursor()


async def create_user_id_and_balance(user_id):
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


async def display_balance(user_id):
    cur.execute("SELECT balance, id FROM user_balance WHERE id = ?", (user_id,))
    entry = cur.fetchone()
    db.commit()
    return entry


async def add_balance(user_id, amount):
    cur.execute("SELECT balance FROM user_balance WHERE id=?", (user_id,))
    cursor_balance = cur.fetchone()[0]
    new_balance = cursor_balance + amount
    cur.execute("UPDATE user_balance SET balance=? WHERE id=?", (new_balance, user_id))
    db.commit()


async def subtract_balance(user_id: int, amount: int):
    cur.execute('SELECT balance FROM user_balance WHERE id=?', (user_id,))
    cur_balance = cur.fetchone()[0]

    if cur_balance >= amount:
        new_balance = cur_balance - amount
        cur.execute('UPDATE user_balance SET balance=? WHERE id=?', (new_balance, user_id))
        db.commit()
    else:
        return None
