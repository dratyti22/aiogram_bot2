import sqlite3 as sq

conn = sq.connect('aiogram2.db')
cur = conn.cursor()


async def create_referral_program_db():
    cur.execute('''CREATE TABLE IF NOT EXISTS referral_program (
        user_id INTEGER PRIMARY KEY,
        link TEXT,
        referrer_id INTEGER,
        clicker_id INTEGER
    )''')
    conn.commit()


async def add_referral_program_db(tg_id: int, link: str):
    cur.execute(
        '''INSERT OR IGNORE INTO referral_program (user_id, link, referrer_id, clicker_id) 
        VALUES (?, ?, ?, ?)''',
        (tg_id, link, 0, 0)
    )
    conn.commit()


async def display_referral_program_db():
    cur.execute('''SELECT * FROM referral_program''')
    entry = cur.fetchall()
    conn.commit()
    return entry


async def change_the_link_db(tg_id: int, link: str):
    cur.execute(
        '''UPDATE referral_program
        SET link = ?
        WHERE user_id = ?''',
        (link, tg_id)
    )
    conn.commit()


async def increase_click_count(referrer_id: int):
    cur.execute(
        "UPDATE referral_program SET whose_links_were_clicked_on = whose_links_were_clicked_on + 1 WHERE user_id = ?",
        (referrer_id,))
    conn.commit()


async def add_clicker(referrer_id: int, clicker_id: int):
    cur.execute("INSERT INTO referral_program (user_id, referrer_id, clicker_id) VALUES (?, ?, ?, ?)",
                (clicker_id, referrer_id, clicker_id,))
    conn.commit()
