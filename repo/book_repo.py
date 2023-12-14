# from postgresql.api import Connection
from sqlite3 import Connection, Cursor

class BookRepo:
    def __init__(self, db: Connection, cursor: Cursor) -> None:
        self.db = db
        self.cursor = cursor

    def get_all(self):
        books = self.cursor.execute("SELECT * FROM books").fetchall()
        return books