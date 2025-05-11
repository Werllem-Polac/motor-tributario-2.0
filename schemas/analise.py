from pydantic import BaseModel
from typing import List

class RequisicaoAnalise(BaseModel):
    cnae: str
    uf: str
    regime_tributario: str

class BeneficioOut(BaseModel):
    nome: str
    descricao: str
    tipo: str

class JurisprudenciaOut(BaseModel):
    titulo: str
    descricao: str
    tribunal: str

class ResultadoAnalise(BaseModel):
    beneficios_aplicaveis: List[BeneficioOut]
    jurisprudencias_aplicaveis: List[JurisprudenciaOut]
    comentarios: List[str]
