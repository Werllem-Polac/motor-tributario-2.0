from fastapi import APIRouter
from typing import List
from schemas.auditoria import DocumentoFiscal, AuditoriaResponse, ResultadoAuditoria
from services.auditor_fiscal import AuditorFiscalInteligente

router = APIRouter()

@router.post("/auditoria/documentos", response_model=AuditoriaResponse)
def auditar_documentos(documentos: List[DocumentoFiscal]):
    fiscal = AuditorFiscalInteligente([doc.dict() for doc in documentos])
    resultado = fiscal.auditar()
    return {"erros_detectados": resultado}
