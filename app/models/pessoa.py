from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base

class Pessoa(Base):
    __tablename__ = 'pessoa'

    id_pessoa = Column(Integer, primary_key=True)
    nome_pessoa = Column(String, nullable=False)
    sobrenome_pessoa = Column(String, nullable=False)
    data_nascimento = Column(String, nullable=False)

    enderecos = relationship("Endereco", back_populates="pessoa")
    telefones = relationship("Telefone", back_populates="pessoa", cascade="all, delete-orphan")
    pedidos = relationship("Pedido", back_populates="pessoa")

