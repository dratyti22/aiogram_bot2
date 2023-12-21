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
    cur.execute('''SELECT balance, id FROM user_balance WHERE id = ?''', (user_id,))
    entry = cur.fetchone()
    db.commit()
    return entry
