"""
Funções de lógica de negócios relacionadas à entidade Empresa.
Contém operações de criação e consulta.
"""

from sqlalchemy.orm import Session
from api.empresas import models, schemas

def criar_empresa(db: Session, empresa: schemas.EmpresaCreate):
    """
    Cria e persiste uma nova empresa no banco de dados.

    Parâmetros:
    - db: sessão do banco
    - empresa: dados da empresa (Pydantic)

    Retorna:
    - Empresa recém criada
    """
    nova = models.Empresa(**empresa.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

def get_empresa_by_id(db: Session, empresa_id: int):
    """
    Retorna uma empresa existente com base no ID.

    Parâmetros:
    - db: sessão do banco
    - empresa_id: ID da empresa

    Retorna:
    - Empresa se encontrada, senão None
    """
    return db.query(models.Empresa).filter(models.Empresa.id == empresa_id).first()
