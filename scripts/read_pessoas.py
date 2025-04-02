from app.repositories.pessoa_repo import get_all_pessoas
from config.database import get_db


db = next(get_db())

pessoas = get_all_pessoas(db)

if not pessoas:
    print("Nenhuma pessoas cadastradas")
else:
    print("Pessoas cadastradas:")
    for pessoa in pessoas:
        print(f"ID: {pessoa.id_pessoa}, Nome: {pessoa.nome_pessoa} {pessoa.sobrenome_pessoa} |"
              f" Data de Nascimento: {pessoa.data_nascimento}")