import sqlite3 as sq

conn = sq.connect('aiogram2.db')
cur = conn.cursor()


def deleted_products_db(db_name, product_id):
    name = '_'.join(db_name.split('_')[:3])
    cur.execute(f'DELETE FROM {name} WHERE id = {product_id}')
    cur.execute(f'UPDATE {name} SET id = id - 1 WHERE id > {product_id}')
    conn.commit()
