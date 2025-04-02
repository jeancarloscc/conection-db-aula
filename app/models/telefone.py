from sqlalchemy import Column, Integer, String
from config.database import Base

class Telefone(Base):
    __tablename__ = 'telefone'

    id_telefone = Column(Integer, primary_key=True, index=True)
    id_pessoa = Column(Integer, nullable=False)
    numero_telefone = Column(String, nullable=False)