from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class Endereco(Base):
    __tablename__ = 'endereco'

    id_endereco = Column(Integer, primary_key=True, index=True)
    id_pessoa = Column(Integer, ForeignKey('pessoa.id_pessoa'))
    cep = Column(String, nullable=False)
    logradouro = Column(String, nullable=False)
    numero = Column(String, nullable=False)
    complemento = Column(String, nullable=False)