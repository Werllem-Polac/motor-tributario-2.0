from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ia_motor.database.engine import SessionLocal
from ia_motor.services import simulador_fiscal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/simular")
def simular(cnpj: str, tese: str, db: Session = Depends(get_db)):
    return simulador_fiscal.simular_por_tese(cnpj, tese, db)

