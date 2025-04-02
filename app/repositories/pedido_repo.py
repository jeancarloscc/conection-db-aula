from sqlalchemy.orm import Session

from app.models.pedido import Pedido


# Criar um novo pedido para uma pessoa
def create_pedido(db: Session, id_pessoa: int, desc_produto: str, valor: float, qtde: int, total: float):
    pedido = Pedido(
        id_pessoa=id_pessoa,
        desc_produto=desc_produto,
        valor_produto=valor,
        quantidade_produto=qtde,
        valor_total=total
    )
    db.add(pedido)
    db.commit()
    db.refresh(pedido)
    return pedido


# Obter todos os pedidos de uma pessoa
def get_pedidos_by_pessoa(db: Session, id_pessoa: int):
    return db.query(Pedido).filter(Pedido.id_pessoa == id_pessoa).all()
