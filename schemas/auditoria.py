from pydantic import BaseModel
from typing import List, Optional

class DocumentoFiscal(BaseModel):
    chave: Optional[str]
    cfop: Optional[str]
    cst: Optional[str]

class ResultadoAuditoria(BaseModel):
    chave: str
    erros: List[str]

class AuditoriaResponse(BaseModel):
    erros_detectados: List[ResultadoAuditoria]
