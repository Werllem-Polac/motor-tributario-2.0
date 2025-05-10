import pandas as pd

def prever_estrategias(dados_notas):
    # Validar entrada
    if dados_notas is None:
        print("[ERRO] Nenhum dado recebido para previsão.")
        return []

    # Se for DataFrame, converter para lista de dicionários
    if isinstance(dados_notas, pd.DataFrame):
        dados_notas = dados_notas.to_dict(orient="records")

    # Se não for lista, erro
    if not isinstance(dados_notas, list):
        print("[ERRO] Formato inválido de dados para previsão.")
        return []

    resultados = []
    for i, nota in enumerate(dados_notas):
        if not isinstance(nota, dict):
            print(f"[AVISO] Ignorando linha {i+1} por formato incorreto: {nota}")
            continue

        cnpj = nota.get("cnpj") or nota.get("CNPJ") or "desconhecido"
        ncm = str(nota.get("NCM", "")).strip()

        # Simples regra de simulação de estratégia
        if ncm.startswith("02"):
            estrategia = "Tese da Desossa + Essencialidade"
            risco = "baixo"
        elif ncm.startswith("05"):
            estrategia = "Subprodutos Imunes"
            risco = "baixo"
        elif ncm.startswith("23"):
            estrategia = "Regime Ração Animal"
            risco = "médio"
        else:
            estrategia = "Análise Manual"
            risco = "alto"

        resultados.append({
            "cnpj": cnpj,
            "produto": nota.get("Produto", "Produto não informado"),
            "ncm": ncm,
            "estrategia": estrategia,
            "risco": risco
        })

    print("📊 Estratégias previstas com sucesso:")
    for r in resultados:
        print(r)

    return resultados

