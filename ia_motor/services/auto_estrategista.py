from ia_motor.services.simulador_fiscal import simular_por_tese

def definir_estrategia(empresa, db):
    teses = ["desoneração insumos", "crédito presumido", "tese da essencialidade"]
    resultados = []

    for tese in teses:
        resultado = simular_por_tese(empresa.cnpj, tese, db)
        if "economia" in resultado:
            resultados.append((tese, resultado["economia"]))

    if not resultados:
        return {"erro": "Nenhuma tese resultou em economia"}

    melhor = max(resultados, key=lambda x: x[1])
    return {
        "melhor_tese": melhor[0],
        "economia_estimada": melhor[1],
        "regime": empresa.regime
    }
