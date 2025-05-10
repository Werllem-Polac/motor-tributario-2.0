def calcular_risco(cnpj: str, dados_fiscais: dict) -> float:
    valor = float(dados_fiscais.get("valor_total", 0) or 0)
    if valor > 100000:
        return 0.85
    elif valor > 50000:
        return 0.6
    elif valor > 10000:
        return 0.35
    else:
        return 0.1


