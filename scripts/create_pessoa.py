from app.repositories.pessoa_repo import create_pessoa
from config.database import get_db
from app.models.pessoa import Pessoa

db = next(get_db())

print("-------- Cadastre uma nova pessoa! -------")
nome = input("Digite o nome da pessoa: ")
sobrenome = input("Digite o sobrenome da pessoa: ")
data_nascimento = input("Digite a data de nascimento da pessoa: ")

try:
    nova_pessoa = Pessoa(nome_pessoa=nome,
                         sobrenome_pessoa=sobrenome,
                         data_nascimento=data_nascimento)
    create_pessoa(db, nova_pessoa)
    print("\033[92m✅ Pessoa cadastrada com sucesso!\033[0m")
except ValueError as e:
    print(f"\033[91m❌ Erro ao cadastrar pessoa:\033[0m: {e}")