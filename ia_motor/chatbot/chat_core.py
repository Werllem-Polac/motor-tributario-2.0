from app.api.ia.prompt_engineering import gerar_prompt
from app.api.database.utils import get_empresa_by_cnpj
from app.api.chatbot.chat_logger import registrar_interacao
from app.api.chatbot.resposta_formatada import formatar_resposta
from app.api.ia.interpretador_legal import gerar_resposta_ia  # novo

def responder_com_contexto(cnpj: str, pergunta: str, db):
    empresa = get_empresa_by_cnpj(db, cnpj)
    if not empresa:
        return "❌ Empresa não encontrada."

    prompt = gerar_prompt(
        tese=pergunta,
        contexto=f"CNPJ: {cnpj}, UF: {empresa.uf}, regime: {empresa.regime}"
    )

    resposta_bruta = gerar_resposta_ia(pergunta, prompt)
    resposta_formatada = formatar_resposta(resposta_bruta, fonte="GPT-4 + Base Legal")

    registrar_interacao(cnpj, pergunta, resposta_formatada)

    return resposta_formatada

