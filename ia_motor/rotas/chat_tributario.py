from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ia_motor.database.engine import SessionLocal
from ia_motor.chatbot import chat_core

router = APIRouter()

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
