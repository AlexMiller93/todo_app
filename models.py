import sqlite3
from datetime import datetime

con = sqlite3.connect("tasks.db")
cur = con.cursor()

# Create the 'items' table if it doesn't exist
cur.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT,
        created_time DATE
    )
''')
con.commit()

# Time management
date_time = datetime.now()
date = date_time.date()  # gives date


class Database:
    @staticmethod
    def drop_and_update():
        cur.execute('DROP TABLE IF EXISTS items')
        cur.execute('''
                    CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        task TEXT,
                        created_time DATE
                    )
                ''')
        con.commit()

    @staticmethod
    def print_all_items():
        cur.execute('SELECT * FROM tasks')
        for row in cur.fetchall():
            print(row[0], row[1], row[2], sep=' -- ')

    @staticmethod
    def add_new_item(item):
        time = str(date.day) + str(date.month) + str(date.year)
        cur.execute(
            'INSERT INTO tasks (task, created_time) VALUES (?, ?)',
            (item, time)
        )
        con.commit()

    @staticmethod
    def remove_item(item_id):
        cur.execute(
            'DELETE FROM tasks WHERE id = ?',
            (item_id,)
        )
        con.commit()

    @staticmethod
    def delete_all_items():
        cur.execute('DELETE FROM tasks')
        con.commit()