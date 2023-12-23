import sqlite3 as sq

conn = sq.connect('aiogram2.db')
cur = conn.cursor()


async def add_product_brawl_stars_db(name: str, price: int):
    cur.execute('''INSERT INTO brawl_stars (name, price) VALUES (?, ?)''', (name, price,))
    conn.commit()
