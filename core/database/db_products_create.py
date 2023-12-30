import sqlite3 as sq

conn = sq.connect('aiogram2.db')
cur = conn.cursor()


async def display_product_pay_in_catalog(name_db: str):
    name = '_'.join(name_db.split('_')[2:])
    id_product = ' '.join(name_db.split('_')[1])
    cur.execute(f'''
        SELECT name,price FROM {name} WHERE id = ?
     ''', (id_product,))
    result = cur.fetchall()
    if result:
        return result
    else:
        return None, None


async def create_brawl_stars_db():
    cur.execute('''CREATE TABLE IF NOT EXISTS brawl_stars(
        id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER
    )''')
    conn.commit()


def display_db(db_name):
    if db_name == 'codm_admin':
        cur.execute(f'''SELECT * FROM codm''')
        entry = cur.fetchall()
        conn.commit()
        return entry
    else:
        name = db_name.rstrip('_admin')
        cur.execute(f'''SELECT * FROM {name}''')
        entry = cur.fetchall()
        conn.commit()
        return entry


def display_brawl_stars_db():
    cur.execute('''SELECT * FROM brawl_stars''')
    entry = cur.fetchall()
    conn.commit()
    return entry


async def create_clash_royale_db():
    cur.execute('''CREATE TABLE IF NOT EXISTS clash_royale(
        id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER
    )''')
    conn.commit()


def display_clash_royale_db():
    cur.execute('''SELECT * FROM clash_royale''')
    entry = cur.fetchall()
    conn.commit()
    return entry


async def create_clash_of_clans_db():
    cur.execute('''CREATE TABLE IF NOT EXISTS clash_of_clans(
        id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER
    )''')
    conn.commit()


def display_clash_of_clans_db():
    cur.execute('''SELECT * FROM clash_of_clans''')
    entry = cur.fetchall()
    conn.commit()
    return entry


async def create_pubg_mobaile_db():
    cur.execute('''CREATE TABLE IF NOT EXISTS pubg_mobaile(
        id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER
    )''')
    conn.commit()


def display_pubg_mobaile_db():
    cur.execute('''SELECT * FROM pubg_mobaile''')
    entry = cur.fetchall()
    conn.commit()
    return entry


async def create_codm_db():
    cur.execute('''CREATE TABLE IF NOT EXISTS codm(
        id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER
    )''')
    conn.commit()


def display_codm_db():
    cur.execute('''SELECT * FROM codm''')
    entry = cur.fetchall()
    conn.commit()
    return entry
