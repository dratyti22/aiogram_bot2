import sqlite3 as sq

conn = sq.connect('aiogram2.db')
cur = conn.cursor()


async def add_product_brawl_stars_db(name: str, price: int):
    cur.execute('''INSERT INTO brawl_stars (name, price) VALUES (?, ?)''', (name, price,))
    conn.commit()


async def add_product_clash_royale_db(name: str, price: int):
    cur.execute('''INSERT INTO clash_royale (name, price) VALUES (?, ?)''', (name, price,))
    conn.commit()


async def add_product_clash_of_clans_db(name: str, price: int):
    cur.execute('''INSERT INTO clash_of_clans (name, price) VALUES (?, ?)''', (name, price,))
    conn.commit()


async def add_product_pubg_mobaile_db(name: str, price: int):
    cur.execute('''INSERT INTO pubg_mobaile (name, price) VALUES (?, ?)''', (name, price,))
    conn.commit()


async def add_product_codm_db(name: str, price: int):
    cur.execute('''INSERT INTO codm (name, price) VALUES (?, ?)''', (name, price,))
    conn.commit()
