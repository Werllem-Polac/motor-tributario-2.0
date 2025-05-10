from fastapi import APIRouter, Depends, HTTPException
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

@router.post("/criar")
def criar_empresa(nome: str, cnpj: str, uf: str = "ES", regime: str = "Lucro Real", db: Session = Depends(get_db)):
    if utils.get_empresa_by_cnpj(db, cnpj):
        raise HTTPException(status_code=400, detail="Empresa já cadastrada.")
    return utils.criar_empresa(db, nome, cnpj, uf, regime)

@router.get("/listar")
def listar_empresas(db: Session = Depends(get_db)):
    return utils.listar_empresas(db)

