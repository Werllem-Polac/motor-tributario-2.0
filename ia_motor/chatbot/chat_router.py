from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ia_motor.database.engine import SessionLocal
from ia_motor.chatbot.chat_core import responder_com_contexto

router = APIRouter()

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

