# api/analise_tributaria/analisador_tributario.py

def analisar_notas(notas):
    # lógica de análise tributária (exemplo fictício)
    resultados = []
    for nota in notas:
        if nota.get("valor", 0) > 1000:
            resultados.append({"nota": nota, "aviso": "valor alto"})
        else:
            resultados.append({"nota": nota, "status": "ok"})
    return resultados
