"""
Modelo de banco de dados (SQLAlchemy) da entidade Empresa.
"""

from sqlalchemy import Column, Integer, String
from api.database.session import Base

class Empresa(Base):
    """
    Representa uma empresa cadastrada no sistema.

    Atributos:
    - id: identificador único
    - nome: nome comercial da empresa
    - cnpj: número do CNPJ
    """
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    cnpj = Column(String, unique=True, index=True)

