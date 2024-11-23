import os
import sqlite3

base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, 'data.db')


db = sqlite3.connect(db_path)
c = db.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone_number TEXT,
    count_of_text_req INT,
    count_of_img_req INT
    )""")
db.commit()

