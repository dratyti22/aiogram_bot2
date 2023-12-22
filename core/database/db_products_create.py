import sqlite3 as sq

conn = sq.connect('aiogram2.db')
cur = conn.cursor()


async def create_brawl_stars_db():
    cur.execute('''CREATE TABLE IF NOT EXISTS brawl_stars(
        id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER
    )''')
    conn.commit()


async def create_clash_royale_db():
    cur.execute('''CREATE TABLE IF NOT EXISTS clash_royale(
        id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER
    )''')
    conn.commit()


async def create_clash_of_clans_db():
    cur.execute('''CREATE TABLE IF NOT EXISTS clash_of_clans(
        id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER
    )''')
    conn.commit()


async def create_pubg_mobaile_db():
    cur.execute('''CREATE TABLE IF NOT EXISTS pubg_mobaile(
        id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER
    )''')
    conn.commit()


async def create_codm_db():
    cur.execute('''CREATE TABLE IF NOT EXISTS codm(
        id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER
    )''')
    conn.commit()
