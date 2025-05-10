from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ia_motor.database.engine import SessionLocal
from ia_motor.database import utils

router = APIRouter()

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
    parecer = f"Empresa {empresa.nome} ({empresa.cnpj}) localizada no estado {empresa.uf}, sob regime {empresa.regime}, possui potencial para recuperação tributária conforme parecer jurídico padrão da IA."
    return {"parecer": parecer}

