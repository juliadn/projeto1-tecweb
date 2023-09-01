import json
from database import *

def extract_route(request):
    return request.split()[1].lstrip('/')

def read_file(path):
    with open(path, 'rb') as f:
        return f.read()
    
def load_data(db):
    return db.get_all()
    
def load_template(file):
    with open('templates/' + file, 'r', encoding='utf-8') as f:
        return str(f.read())
    
def adiciona(params):
    with open('data/notes.json', 'r') as f:
        text = f.read()
        notes = json.loads(text)
        notes.append(params)
    with open('data/notes.json', 'w') as f:
        f.write(json.dumps(notes, indent=4, ensure_ascii=False))
    
def build_response(body='', code=200, reason='OK', headers=''):
    if headers == '':
        response = "HTTP/1.1 " + str(code) + " " + reason + "\n\n" + body
    else:
        response = "HTTP/1.1 " + str(code) + " " + reason + "\n" + headers + "\n\n" + body
    
    return str(response).encode()
