from sqlalchemy.orm import Session
from ia_motor.database import models

def get_empresa_by_cnpj(db: Session, cnpj: str):
    return db.query(models.Empresa).filter(models.Empresa.cnpj == cnpj).first()

def criar_empresa(db: Session, nome: str, cnpj: str, uf: str = "ES", regime: str = "Lucro Real"):
    nova = models.Empresa(
        nome=nome,
        cnpj=cnpj,
        uf=uf,
        regime=regime
    )
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

def listar_empresas(db: Session):
    return db.query(models.Empresa).all()

def salvar_documento(db: Session, empresa_id: int, tipo: str, nome_arquivo: str, conteudo: str = ""):
    doc = models.DocumentoFiscal(
        empresa_id=empresa_id,
        tipo=tipo,
        nome_arquivo=nome_arquivo,
        conteudo=conteudo
    )
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc

def registrar_analise(db: Session, empresa_id: int, tese: str, economia: float, risco: float, parecer: str):
    analise = models.AnaliseFiscal(
        empresa_id=empresa_id,
        tese_sugerida=tese,
        economia_estimativa=economia,
        risco_percentual=risco,
        parecer=parecer
    )
    db.add(analise)
    db.commit()
    db.refresh(analise)
    return analise

