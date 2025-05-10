from datetime import datetime

# Simulação de log — pode ser armazenado em DB ou arquivo futuramente
logs = []

def registrar_interacao(cnpj: str, pergunta: str, resposta: str):
    log = {
        "cnpj": cnpj,
        "pergunta": pergunta,
        "resposta": resposta,
        "timestamp": datetime.utcnow().isoformat()
    }
    logs.append(log)
    print("💬 LOG INTERAÇÃO:", log)

def consultar_logs(cnpj: str) -> list:
    return [log for log in logs if log["cnpj"] == cnpj]

