from app.repositories.pessoa_repo import delete_pessoa
from config.database import get_db

db = next(get_db())

print("-------- Deletar uma pessoa! -------")
id_pessoa = int(input("Digite o ID do pessoa que deseja deletar: "))

delete_pessoa(db, id_pessoa)