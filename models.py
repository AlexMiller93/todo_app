import sqlite3

from tkinter import filedialog

from const import *

con = sqlite3.connect("tasks.db")
cur = con.cursor()

# Create the 'tasks' table if it doesn't exist
cur.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT,
        created_time DATE
    )
''')
con.commit()



class Database:

    @staticmethod
    def print_all_items():
        cur.execute('SELECT * FROM tasks')
        for row in cur.fetchall():
            print(row[0], row[1], row[2], sep=' -- ')

    @staticmethod
    def save_data_in_file():
        with open(f"{FOLDER}Tasks_{MONTH}_{DAY}.txt", "w") as file:
            # file content
            cur.execute('SELECT * FROM tasks')
            file.write(f"Your tasks {DATE.day} {MONTH}\n")
            for row in cur.fetchall():
                file.write(f"{row}\n")
        
        

    @staticmethod
    def add_new_item(item):
        timestamp = f"{MIN}:{HOUR} {DAY} {MONTH} - {WK_DAY}"
        cur.execute(
            'INSERT INTO tasks (task, created_time) VALUES (?, ?)',
            (item, timestamp)
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
        
    @staticmethod
    def count_items():
        cur.execute('SELECT COUNT(*) FROM tasks')
        result = cur.fetchone()
        row_count = result[0]
        con.commit()
        
        return row_count