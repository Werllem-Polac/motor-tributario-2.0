from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.models import CNAE, BeneficioFiscal, Jurisprudencia
from schemas.schemas import CNAECreate, CNAEOut, BeneficioCreate, BeneficioOut, JurisprudenciaCreate, JurisprudenciaOut

router = APIRouter()

@router.post("/cnaes", response_model=CNAEOut)
def create_cnae(cnae: CNAECreate, db: Session = Depends(get_db)):
    db_cnae = CNAE(**cnae.dict())
    db.add(db_cnae)
    db.commit()
    db.refresh(db_cnae)
    return db_cnae

@router.get("/cnaes", response_model=list[CNAEOut])
def list_cnaes(db: Session = Depends(get_db)):
    return db.query(CNAE).all()

@router.post("/beneficios", response_model=BeneficioOut)
def create_beneficio(beneficio: BeneficioCreate, db: Session = Depends(get_db)):
    db_beneficio = BeneficioFiscal(**beneficio.dict())
    db.add(db_beneficio)
    db.commit()
    db.refresh(db_beneficio)
    return db_beneficio

@router.get("/beneficios", response_model=list[BeneficioOut])
def list_beneficios(db: Session = Depends(get_db)):
    return db.query(BeneficioFiscal).all()

@router.post("/jurisprudencias", response_model=JurisprudenciaOut)
def create_jurisprudencia(juris: JurisprudenciaCreate, db: Session = Depends(get_db)):
    db_juris = Jurisprudencia(**juris.dict())
    db.add(db_juris)
    db.commit()
    db.refresh(db_juris)
    return db_juris

@router.get("/jurisprudencias", response_model=list[JurisprudenciaOut])
def list_jurisprudencias(db: Session = Depends(get_db)):
    return db.query(Jurisprudencia).all()
