import sqlite3 as sq

conn = sq.connect('aiogram2.db')
cur = conn.cursor()


async def save_orders_db(name_products: str, price_products: int, time_products: str, id_product: str,
                         email_products: str):
    cur.execute('''CREATE TABLE IF NOT EXISTS orders(
        id_products INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER,
        time TEXT,
        id TEXT,
        email TEXT
    )''')
    conn.commit()
    cur.execute('''INSERT INTO orders(name, price, time, id, email) VALUES (?, ?, ?, ?, ?)''',
                (name_products, price_products, time_products, id_product, email_products))
    conn.commit()


def display_orders_db():
    cur.execute('''SELECT id_products,name,price,time,id FROM orders''')
    entry = cur.fetchall()
    conn.commit()
    return entry


async def display_orders_id_db(product_id):
    cur.execute("SELECT name, price, time, id FROM orders WHERE id_products =?", (product_id,))
    result = cur.fetchall()
    return result
