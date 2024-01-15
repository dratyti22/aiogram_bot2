import sqlite3 as sq

conn = sq.connect('aiogram2.db')
cur = conn.cursor()


async def create_orders_db():
    cur.execute('''CREATE TABLE IF NOT EXISTS orders(
        id_products INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER,
        time TEXT,
        id TEXT,
        email TEXT,
        payment TEXT
    )''')
    conn.commit()


async def save_orders_db(name_products: str, price_products: int, time_products: str, id_product: str,
                         email_products: str, payment_products: str):
    cur.execute('''INSERT INTO orders(name, price, time, id, email, payment) VALUES (?, ?, ?, ?, ?, ?)''',
                (name_products, price_products, time_products, id_product, email_products, payment_products,))
    conn.commit()


def display_orders_db():
    cur.execute('''SELECT id_products,name,price,time,id, payment FROM orders''')
    entry = cur.fetchall()
    conn.commit()
    return entry


async def display_orders_id_db(product_id):
    cur.execute("SELECT name, price, time, id FROM orders WHERE id_products =?", (product_id,))
    result = cur.fetchall()
    return result


def change_email_db(id_product, new_email):
    cur.execute('UPDATE orders SET email=? WHERE id=?', (new_email, id_product,))
    conn.commit()
