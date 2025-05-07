from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UsuarioCreateSchema(BaseModel):
    email: EmailStr
    senha: str

class UsuarioLoginSchema(BaseModel):
    email: EmailStr
    senha: str

class EmpresaSchema(BaseModel):
    razao_social: str
    cnpj: str
    dono_id: Optional[int] = None

    class Config:
        orm_mode = True

class ProdutoSchema(BaseModel):
    nome: str
    valor: float
    empresa_id: int

    class Config:
        orm_mode = True

class PerguntaIASchema(BaseModel):
    pergunta: str
    resposta: Optional[str] = None
    cnpj: str
    empresa_id: int
    criada_em: Optional[datetime] = None

    class Config:
        orm_mode = True
