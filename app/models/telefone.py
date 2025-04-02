from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base

class Telefone(Base):
    __tablename__ = 'telefone'

    id_telefone = Column(Integer, primary_key=True, autoincrement=True)
    id_pessoa = Column(Integer, ForeignKey("pessoa.id_pessoa", ondelete="CASCADE"), nullable=False)
    numero_telefone = Column(String, nullable=False)

    pessoa = relationship("Pessoa", back_populates="telefones")