import sqlite3 as sq

conn = sq.connect('aiogram2.db')
cur = conn.cursor()


async def create_coupons():
    cur.execute('''CREATE TABLE IF NOT EXISTS coupons (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER,
        quantity INTEGER
    )''')
    conn.commit()


async def add_coupons(name: str, price: int, quantity: int):
    cur.execute("INSERT INTO coupons (name, price, quantity) VALUES (?, ?, ?)", (name, price, quantity,))
    conn.commit()


async def deleted_coupons(id_coupons):
    cur.execute("DELETE FROM coupons WHERE id=?", (id_coupons,))
    cur.execute("UPDATE coupons SET id = id - 1 WHERE id > ?", (id_coupons,))
    conn.commit()


async def display_coupons():
    cur.execute("SELECT * FROM coupons")
    entry = cur.fetchall()
    conn.commit()
    return entry


async def get_coupon_details(coupon_name: str):
    cur.execute("SELECT price, quantity FROM coupons WHERE name = ?", (coupon_name,))
    result = cur.fetchone()
    if result:
        return result
    return None, None


async def decrement_coupon_amount(coupon_name: str):
    cur.execute("UPDATE coupons SET quantity = quantity - 1 WHERE name = ?", (coupon_name,))
    conn.commit()
