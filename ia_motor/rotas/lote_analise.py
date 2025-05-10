from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ia_motor.database.engine import SessionLocal
from ia_motor.database import utils
from ia_motor.services import auto_estrategista

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/executar")
def executar_lote(cnpjs: list[str], db: Session = Depends(get_db)):
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
