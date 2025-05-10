# ia_motor/ia/interpretador_legal.py

from ia_motor.ia.prompt_engineering import gerar_prompt

def gerar_resposta_ia(tese: str, contexto: str) -> str:
    prompt = gerar_prompt(tese, contexto)
    # Aqui você pode integrar com OpenAI, Google Palm, ou LLM local
    return (
        f"🧠 Análise automatizada para a tese: {tese}\n"
        f"Contexto: {contexto}\n"
        f"Fonte: Simulação interna com base jurídica."
    )
