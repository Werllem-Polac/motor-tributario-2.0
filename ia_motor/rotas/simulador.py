from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.database.session import SessionLocal
from app.api.services import simulador_fiscal  # ajuste conforme o local real do script

router = APIRouter()

# Dependência do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/simular")
def simular(cnpj: str, tese: str, db: Session = Depends(get_db)):
    return simulador_fiscal.simular_por_tese(cnpj, tese, db)


