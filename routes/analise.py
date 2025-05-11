from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from services.motor_regras import MotorRegrasTributarias
from schemas.analise import RequisicaoAnalise, ResultadoAnalise

router = APIRouter()

@router.post("/analise/empresa", response_model=ResultadoAnalise)
def analisar_empresa(dados: RequisicaoAnalise, db: Session = Depends(get_db)):
    motor = MotorRegrasTributarias(
        db=db,
        cnae=dados.cnae,
        uf=dados.uf,
        regime=dados.regime_tributario
    )
    resultado = motor.analisar()
    return resultado
