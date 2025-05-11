from fastapi import APIRouter
from pydantic import BaseModel
from api.services.inteligencia_tributaria import analisar_texto_empresa

router = APIRouter(prefix="/ia/juridica", tags=["IA Jurídica"])

class TextoEntrada(BaseModel):
    texto: str

@router.post("/classificar")
def classificar_ia_juridica(payload: TextoEntrada):
    return analisar_texto_empresa(payload.texto)
