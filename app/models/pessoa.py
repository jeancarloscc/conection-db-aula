from sqlalchemy import Column, Integer, String
from config.database import Base

class Pessoa(Base):
    __tablename__ = 'pessoa'

    id_pessoa = Column(Integer, primary_key=True)
    nome_pessoa = Column(String, nullable=False)
    sobrenome_pessoa = Column(String, nullable=False)
    data_nascimento = Column(String, nullable=False)

