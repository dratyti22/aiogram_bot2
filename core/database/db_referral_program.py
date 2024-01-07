import sqlite3 as sq

conn = sq.connect('aiogram2.db')
cur = conn.cursor()


async def create_referral_program_db(tg_id: int, link: str):
    cur.execute(
        '''CREATE TABLE IF NOT EXISTS referral_program (
        user_id INTEGER PRIMARY KEY,
        link TEXT,
        price INTEGER,
        who_clicked_on_the_ink INTEGER
        )'''
    )
    conn.commit()

    cur.execute(
        '''INSERT OR IGNORE INTO referral_program (user_id, link, price, who_clicked_on_the_ink) 
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
