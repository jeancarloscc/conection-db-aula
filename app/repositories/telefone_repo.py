from sqlalchemy.orm import Session

from app.models.telefone import Telefone


# Criar um novo telefone para uma pessoa
def create_telefone(db: Session, id_pessoa: int, numero: str):
    telefone = Telefone(id_pessoa=id_pessoa, numero_telefone=numero)
    db.add(telefone)
    db.commit()
    db.refresh(telefone)
    return telefone


# Obter todos os telefones de uma pessoa
def get_telefones_by_pessoa(db: Session, id_pessoa: int):
    return db.query(Telefone).filter(Telefone.id_pessoa == id_pessoa).all()
