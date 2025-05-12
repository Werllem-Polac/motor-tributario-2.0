from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.database.session import SessionLocal
from app.api.chatbot.chat_core import responder_com_contexto

router = APIRouter()

# Dependência de sessão com o banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/responder")
def responder(cnpj: str, pergunta: str, db: Session = Depends(get_db)):
    resposta = responder_com_contexto(cnpj, pergunta, db)
    return {"resposta": resposta}
