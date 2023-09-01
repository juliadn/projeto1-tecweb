import sqlite3
from dataclasses import dataclass

class Database: 

    def __init__(self, data):

        self.conn = sqlite3.connect(data + '.db')
        self.conn.execute("CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL)")
        self.cursor = self.conn.cursor()

    def add(self, note):
        insert_query = "INSERT INTO note (title, content) VALUES (?, ?)"
        values = (note.title, note.content)
        self.conn.execute(insert_query, values)
        self.conn.commit()

    def update(self, entry):
        self.cursor.execute(
            'UPDATE note SET title = ?, content = ? WHERE id = ?', (entry.title, entry.content, entry.id))
        self.conn.commit()

    def get_all(self):
        cursor = self.conn.execute(
            "SELECT id, title, content FROM note")
        lista = []
        for linha in cursor:
            id = linha[0]
            title = linha[1]
            content = linha[2]
            lista.append(Note(id, title, content))

        return lista
    def delete(self, note_id):
        self.cursor.execute('DELETE FROM note WHERE id = ?', (note_id,))
        self.conn.commit()

    def get(self, index):
        cursor = self.conn.execute(
            "SELECT id, title, content FROM note")
        
        for linha in cursor:
            id = linha[0]
            title = linha[1]
            content = linha[2]
            if id == index:
                return Note(id=id, title=title, content=content)
        return None

    

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

        