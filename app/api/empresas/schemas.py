"""
Modelos de validação e serialização Pydantic para a entidade Empresa.
"""

from pydantic import BaseModel

class EmpresaBase(BaseModel):
    """
    Atributos comuns para criação e leitura de empresa.
    """
    nome: str
    cnpj: str

class EmpresaCreate(EmpresaBase):
    """
    Esquema para criação de empresa.
    """
    pass

class Empresa(EmpresaBase):
    """
    Esquema de resposta da empresa, incluindo ID.
    """
    id: int

    class Config:
        orm_mode = True  # Permite leitura a partir de ORM (SQLAlchemy)
