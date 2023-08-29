import sqlite3
from dataclasses import dataclass

class Database: 

    def __init__(self, data):

        self.conn = sqlite3.connect(data + '.db')
        self.conn.execute("CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL)")

    def add(self, note):
        insert_query = "INSERT INTO note (title, content) VALUES (?, ?)"
        values = (note.title, note.content)
        self.conn.execute(insert_query, values)
        self.conn.commit()

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

        