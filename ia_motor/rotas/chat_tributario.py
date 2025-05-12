from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.database.session import SessionLocal
from app.api.chatbot import chat_core  # ajuste conforme sua estrutura real

router = APIRouter()

# Dependência de sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/perguntar")
def perguntar(cnpj: str, pergunta: str, db: Session = Depends(get_db)):
    resposta = chat_core.responder_com_contexto(cnpj, pergunta, db)
    return {"resposta": resposta}

