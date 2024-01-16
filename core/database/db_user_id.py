import sqlite3 as sq

db = sq.connect('aiogram2.db')
cur = db.cursor()


async def start_user_id_db(user_id):
    cur.execute('''CREATE TABLE IF NOT EXISTS accounts (
    tg_id INTEGER PRIMARY KEY, 
    activate INTEGER
    )''')
    user = cur.execute("SELECT * FROM accounts WHERE tg_id == {key}".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO accounts (tg_id) VALUES ({key})".format(key=user_id))
        db.commit()


def set_activate_db(user_id, activate):
    return cur.execute(
        '''UPDATE accounts SET activate = {key} WHERE tg_id == {key2}'''.format(key=activate, key2=user_id))


def get_users_db():
    return cur.execute("SELECT tg_id, activate FROM accounts").fetchall()


def search_user_id_db(user_id):
    cur.execute("SELECT * FROM accounts WHERE tg_id = ?", (user_id,))
    result = cur.fetchone()
    return result is not None
