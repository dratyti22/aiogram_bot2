import sqlite3 as sq

db = sq.connect('aiogram2.db')
cur = db.cursor()


async def start_user_id_db(user_id):
    cur.execute("CREATE TABLE IF NOT EXISTS accounts (tg_id INTEGER PRIMARY KEY), activate INTEGER")
    user = cur.execute("SELECT * FROM accounts WHERE tg_id == {key}".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO accounts (tg_id) VALUES ({key})".format(key=user_id))
        db.commit()
