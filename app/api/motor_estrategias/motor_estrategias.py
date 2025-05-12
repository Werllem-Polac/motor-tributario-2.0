# api/motor_estrategias/motor_estrategias.py

def gerar_estrategias(dados_fiscais):
    """
    Função fictícia para gerar estratégias com base nos dados fornecidos.
    """
    if dados_fiscais is None or dados_fiscais.empty:
        return {"status": "sem dados para estratégia"}

    return {
        "estrategias": [
            {"nome": "Crédito ICMS Energia", "aplicável": True},
            {"nome": "Diferimento ICMS Entrada", "aplicável": False}
        ],
        "status": "estratégias geradas com sucesso"
    }
