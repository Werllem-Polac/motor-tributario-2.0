from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID
from datetime import date

class CNAEBase(BaseModel):
    codigo_cnae: str
    descricao: str
    tipo_atividade: str

class CNAECreate(CNAEBase):
    pass

class CNAEOut(CNAEBase):
    id: UUID
    class Config:
        orm_mode = True

class BeneficioBase(BaseModel):
    nome: str
    tipo: str
    descricao: Optional[str]
    abrangencia_uf: List[str]
    ativo: bool = True

class BeneficioCreate(BeneficioBase):
    pass

class BeneficioOut(BeneficioBase):
    id: UUID
    class Config:
        orm_mode = True

class JurisprudenciaBase(BaseModel):
    titulo: str
    descricao: Optional[str]
    tribunal: str
    link_documento: Optional[str]
    uf: Optional[str]
    data_publicacao: Optional[date]

class JurisprudenciaCreate(JurisprudenciaBase):
    pass

class JurisprudenciaOut(JurisprudenciaBase):
    id: UUID
    class Config:
        orm_mode = True
