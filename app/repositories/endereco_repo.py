from sqlalchemy.orm import Session

from app.models.endereco import Endereco


# Criar um novo endereço para uma pessoa
def create_endereco(db: Session, id_pessoa: int, cep: str, logradouro: str, numero: int, complemento: str = None):
    endereco = Endereco(
        id_pessoa=id_pessoa,
        cep=cep,
        logradouro=logradouro,
        numero=numero,
        complemento=complemento
    )
    db.add(endereco)
    db.commit()
    db.refresh(endereco)
    return endereco


# Obter todos os endereços de uma pessoa
def get_enderecos_by_pessoa(db: Session, id_pessoa: int):
    return db.query(Endereco).filter(Endereco.id_pessoa == id_pessoa).all()
