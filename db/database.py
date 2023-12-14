# '''Postgresql module'''
# import postgresql
# from postgresql.api import Connection

# def start_db():
#     db = postgresql.open('pq://office:xR7B075mONwM@localhost:5430/book_platform')    
#     migrate(db)
#     return db

# def migrate(db: Connection):
#     db.prepare('''CREATE TABLE IF NOT EXISTS book (
#         id SERIAL NOT NULL PRIMARY KEY,
#         title VARCHAR(255) NOT NULL,
#         author VARCHAR(255) NOT NULL,
#         created_at DATETIME NOT NULL)''')

import sqlite3

def start_db():
    db = sqlite3.connect("./db/books.db")
    cursor = db.cursor()
    migrate(db, cursor)
    return db, cursor

def migrate(db: sqlite3.Connection, cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(255) NOT NULL,
        author VARCHAR(255) NOT NULL,
        created_at TIMESTAMP NOT NULL)''')
    db.commit()