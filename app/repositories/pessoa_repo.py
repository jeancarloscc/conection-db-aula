from sqlalchemy.orm import Session

from app.models.endereco import Endereco
from app.models.pessoa import Pessoa

def create_pessoa(db: Session, pessoa: Pessoa):
    db.add(pessoa)
    db.commit()
    db.refresh(pessoa)
    return pessoa

def get_all_pessoas(db: Session):
    return db.query(Pessoa).all()

def get_pessoa_by_id(db: Session, id_pessoa: int):
    return db.query(Pessoa).filter(Pessoa.id_pessoa == id_pessoa).first()

def update_pessoa(db: Session, pessoa_id: int, nome: str = None, sobrenome: str = None, data_nascimento: str = None):
    pessoa = db.query(Pessoa).filter_by(id_pessoa=pessoa_id).first()
    if not pessoa:
        return None
    if nome:
        pessoa.nome_pessoa = nome
    if sobrenome:
        pessoa.sobrenome_pessoa = sobrenome
    if data_nascimento:
        pessoa.data_nascimento = data_nascimento
    db.commit()
    db.refresh(pessoa)
    return pessoa


def delete_pessoa(db: Session, pessoa_id: int):
    # Primeiro, verificar e apagar os registros relacionados na tabela "endereco"
    db.query(Endereco).filter(Endereco.id_pessoa == pessoa_id).delete()

    # Depois, apagar o registro da tabela "pessoa"
    pessoa = db.query(Pessoa).filter_by(id_pessoa=pessoa_id).first()
    if pessoa:
        db.delete(pessoa)
        db.commit()
    return pessoa

