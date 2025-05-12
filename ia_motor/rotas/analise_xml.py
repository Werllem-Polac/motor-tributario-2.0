from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.database.session import SessionLocal
from app.api.database import utils
import uuid

router = APIRouter()

# Dependência de sessão com o banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload/")
def upload_xml(
    cnpj: str,
    tipo: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    empresa = utils.get_empresa_by_cnpj(db, cnpj)
    if not empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada.")

    conteudo = file.file.read().decode("utf-8")
    nome_arquivo = f"{uuid.uuid4()}_{file.filename}"

    utils.salvar_documento(db, empresa.id, tipo, nome_arquivo, conteudo)
    
    return {"mensagem": "Arquivo salvo com sucesso", "arquivo": nome_arquivo}


