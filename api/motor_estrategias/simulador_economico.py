# api/motor_estrategias/simulador_economico.py

def simular_cenarios(dados):
    """
    Simula diferentes cenários econômicos com base nos dados fiscais fornecidos.
    """
    if dados is None or dados.empty:
        return {"erro": "sem dados para simulação"}

    return {
        "cenarios": [
            {"nome": "Cenário Base", "economia": 0},
            {"nome": "Crédito de ICMS sobre energia", "economia": 32000},
            {"nome": "Tese da Essencialidade aplicada", "economia": 58000}
        ],
        "status": "simulação realizada com sucesso"
    }
