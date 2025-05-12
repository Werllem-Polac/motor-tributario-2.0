from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List  # Corrige tipagem do FastAPI
from app.api.database.session import SessionLocal
from app.api.database import utils
from app.api.services import auto_estrategista  # ajuste o caminho conforme sua estrutura

router = APIRouter()

# Dependência do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/executar")
def executar_lote(cnpjs: List[str], db: Session = Depends(get_db)):
    resultados = []
    for cnpj in cnpjs:
        empresa = utils.get_empresa_by_cnpj(db, cnpj)
        if empresa:
            estrategia = auto_estrategista.definir_estrategia(empresa, db)
            resultados.append({
                "cnpj": cnpj,
                "empresa": empresa.nome,
                "estrategia": estrategia
            })
    return resultados

