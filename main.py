from sqlalchemy.orm import Session
from config.database import get_db, engine, Base
from app.repositories.pessoa_repo import create_pessoa, get_all_pessoas
from app.repositories.endereco_repo import create_endereco, get_enderecos_by_pessoa
from app.repositories.telefone_repo import create_telefone, get_telefones_by_pessoa
from app.repositories.pedido_repo import create_pedido, get_pedidos_by_pessoa

# Certifique-se de criar as tabelas no banco de dados
Base.metadata.create_all(bind=engine)


# Função principal para adicionar registros
def criar_pessoa_completa(db: Session):
    from app.models.pessoa import Pessoa  # Certifique-se de ter a classe correta importada

    # Capturar as informações da pessoa via formulário
    print("=== Formulário para Cadastro de Pessoa ===")
    nome_pessoa = input("Digite o nome da pessoa: ").strip()
    sobrenome_pessoa = input("Digite o sobrenome da pessoa: ").strip()
    data_nascimento = input("Digite a data de nascimento (no formato YYYY-MM-DD): ").strip()

    # Criar o objeto Pessoa
    nova_pessoa = Pessoa(
        nome_pessoa=nome_pessoa,
        sobrenome_pessoa=sobrenome_pessoa,
        data_nascimento=data_nascimento
    )

    # Salvar a pessoa no banco de dados
    pessoa = create_pessoa(db, nova_pessoa)
    print(f"\nPessoa '{pessoa.nome_pessoa} {pessoa.sobrenome_pessoa}' cadastrada com sucesso!")

    # === Capturar informações de endereço ===
    print("\n=== Formulário para Cadastro de Endereços ===")
    while True:
        cep = input("Digite o CEP: ").strip()
        logradouro = input("Digite o logradouro: ").strip()
        numero = input("Digite o número: ").strip()
        complemento = input("Digite o complemento (opcional): ").strip()

        create_endereco(db, pessoa.id_pessoa, cep=cep, logradouro=logradouro, numero=numero, complemento=complemento)
        print("Endereço cadastrado com sucesso!")

        adicionar_mais = input("Deseja adicionar outro endereço? (s/n): ").strip().lower()
        if adicionar_mais != 's':
            break

    # === Capturar informações de telefone ===
    print("\n=== Formulário para Cadastro de Telefones ===")
    while True:
        numero_telefone = input("Digite o número de telefone: ").strip()
        create_telefone(db, pessoa.id_pessoa, numero=numero_telefone)
        print("Telefone cadastrado com sucesso!")

        adicionar_mais = input("Deseja adicionar outro telefone? (s/n): ").strip().lower()
        if adicionar_mais != 's':
            break

    # === Capturar informações de pedidos ===
    print("\n=== Formulário para Cadastro de Pedidos ===")
    while True:
        desc_produto = input("Digite a descrição do produto: ").strip()
        valor = float(input("Digite o valor do produto: ").strip())
        qtde = int(input("Digite a quantidade: ").strip())
        total = valor * qtde

        create_pedido(db, pessoa.id_pessoa, desc_produto=desc_produto, valor=valor, qtde=qtde, total=total)
        print("Pedido cadastrado com sucesso!")

        adicionar_mais = input("Deseja adicionar outro pedido? (s/n): ").strip().lower()
        if adicionar_mais != 's':
            break

    # Retornar a pessoa criada
    return pessoa




# Função para listar informações completas
def listar_pessoa_com_dados(db: Session, id_pessoa: int):
    # Pessoa
    pessoa = get_all_pessoas(db)[0]

    # Endereços
    enderecos = get_enderecos_by_pessoa(db, pessoa.id_pessoa)

    # Telefones
    telefones = get_telefones_by_pessoa(db, pessoa.id_pessoa)

    # Pedidos
    pedidos = get_pedidos_by_pessoa(db, pessoa.id_pessoa)

    print(f"Pessoa: {pessoa.nome_pessoa} {pessoa.sobrenome_pessoa} (ID: {pessoa.id_pessoa})")
    print("-" * 50)

    print("Endereços:")
    for endereco in enderecos:
        print(f"  - CEP: {endereco.cep}, Logradouro: {endereco.logradouro}, Número: {endereco.numero}")

    print("\nTelefones:")
    for telefone in telefones:
        print(f"  - Número: {telefone.numero_telefone}")

    print("\nPedidos:")
    for pedido in pedidos:
        print(
            f"  - Produto: {pedido.desc_produto}, Valor: {pedido.valor_produto}, Quantidade: {pedido.quantidade_produto}, Total: {pedido.valor_total}")


# Executar o programa principal
def main():
    db: Session = next(get_db())

    print("Criando registros...")
    pessoa = criar_pessoa_completa(db)

    print("\nListando informações da pessoa...")
    listar_pessoa_com_dados(db, pessoa.id_pessoa)


if __name__ == "__main__":
    main()


