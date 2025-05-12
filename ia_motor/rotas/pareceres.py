from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.database.session import SessionLocal
from app.api.database import utils

router = APIRouter()

# Dependência de sessão com o banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/gerar")
def gerar_parecer(cnpj: str, db: Session = Depends(get_db)):
    empresa = utils.get_empresa_by_cnpj(db, cnpj)
    if not empresa:
        return {"erro": "Empresa não encontrada."}
    
    parecer = (
        f"Empresa {empresa.nome} ({empresa.cnpj}) localizada no estado {empresa.uf}, "
        f"sob regime {empresa.regime}, possui potencial para recuperação tributária "
        f"conforme parecer jurídico padrão da IA."
    )

    return {"parecer": parecer}

