import sqlite3 as sq

conn = sq.connect('aiogram2.db')
cur = conn.cursor()


async def save_orders_db(name_products: str, price_products: int, time_products: str, id_products: str,
                         email_products: str):
    cur.execute('''CREATE TABLE IF NOT EXISTS orders(
        name TEXT,
        price INTEGER
        time TEXT,
        id TEXT
        email TEXT
    )''')
    conn.commit()
    cur.execute('''INSERT INTO orders(name, price, time, id, email) VALUES (?, ?, ?, ?, ?)''',
                (name_products, price_products, time_products, id_products, email_products))
    conn.commit()


async def get_orders_db():
    cur.execute('''SELECT name FROM orders''')
    entry = cur.fetchall()
    conn.commit()
    return entry
