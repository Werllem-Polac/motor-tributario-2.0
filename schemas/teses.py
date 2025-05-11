from pydantic import BaseModel
from typing import List

class RequisicaoClassificacao(BaseModel):
    cnae: str
    uf: str
    regime_tributario: str

class ResultadoClassificacao(BaseModel):
    tipo_empresa: str
    teses_recomendadas: List[str]
