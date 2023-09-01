from utils import load_data, load_template, adiciona, build_response
from database import Note, Database
from urllib.parse import unquote_plus


def index(request):
    # A string de request sempre começa com o tipo da requisição (ex: GET, POST)
    db = Database('data/banco')
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[-1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        
        if corpo != "":
            chave_valor =  corpo.split('&')
            esquerda = chave_valor[0].split('=')
            direita = chave_valor[1].split('=')
            titulo = unquote_plus(esquerda[1])
            conteudo = unquote_plus(direita[1])
            params[titulo] = conteudo

        db.add(Note(title=titulo, content=conteudo))

        return build_response(code=303, reason='See Other', headers='Location:/')

    # Cria uma lista de <li>'s para cada anotação
    # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados.title, details=dados.content, id=dados.id)
        for dados in load_data(db)
    ]
    notes = '\n'.join(notes_li)

    body = load_template('index.html').format(notes=notes)

    return build_response(body=body)

#vai alterar o banco de dados e mudar apenas o conteudo
def edit(request, id):
    db = Database('data/banco')
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        partes = request.split('\n\n')
        corpo = partes[-1]
        params = {}
        if corpo != "":
            chave_valor =  corpo.split('&')
            esquerda = chave_valor[0].split('=')
            direita = chave_valor[1].split('=')
            titulo = unquote_plus(esquerda[1])
            conteudo = unquote_plus(direita[1])
            params[titulo] = conteudo

        db.update(Note(
            id = id,
            title=titulo,
            content=conteudo
        ))

        return build_response(code=303, reason='See Other', headers='Location:/')

    note = db.get(id)
    body = load_template('edit.html').format(
        id=id,
        title=note.title,
        details=note.content
    )
    return build_response(body=body)

#deleta o conteudo do banco de dados
def delete(id):
    db = Database('data/banco')
    db.delete(id)
    return build_response(code=303, reason='See Other', headers='Location:/')