from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from config.database import Base

class Pedido(Base):
    __tablename__ = 'pedido'

    id_pedido = Column(Integer, primary_key=True, index=True)
    id_pessoa = Column(Integer, ForeignKey('pessoa.id_pessoa'))
    desc_produto = Column(String, nullable=False)
    valor_produto = Column(Float, nullable=False)
    quantidade_produto = Column(Integer, nullable=False)
    valor_total = Column(Float, nullable=False)

    pessoa = relationship("Pessoa", back_populates="pedidos")