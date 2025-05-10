import pandas as pd

def treinar_ia(dados):
    print("\n Iniciando treinamento da IA com os dados disponíveis...")

    # Validar estrutura de dados
    if dados is None:
        print("[ERRO] Nenhum dado recebido.")
        return

    if isinstance(dados, pd.DataFrame):
        dados = dados.to_dict(orient="records")

    if not isinstance(dados, list):
        print("[ERRO] Formato inválido para treinamento.")
        return

    aprendizados = []

    for i, linha in enumerate(dados):
        if not isinstance(linha, dict):
            print(f"[AVISO] Ignorando linha inválida #{i+1}: {linha}")
            continue

        cnpj = linha.get("cnpj") or linha.get("CNPJ") or "desconhecido"
        produto = linha.get("Produto", "desconhecido")
        ncm = str(linha.get("NCM", "")).strip()
        cfop = str(linha.get("CFOP", "")).strip()
        cst = str(linha.get("CST", "não informado")).strip()

        if not ncm:
            print(f"[AVISO] Linha {i+1} sem NCM. Ignorada.")
            continue

        # Lógica simulada de aprendizado
        estrategia_aprendida = None
        if ncm.startswith("02"):
            estrategia_aprendida = "Tese da Desossa + Essencialidade"
        elif ncm.startswith("05"):
            estrategia_aprendida = "Subprodutos Imunes"
        elif ncm.startswith("23"):
            estrategia_aprendida = "Regime Ração Animal"
        else:
            estrategia_aprendida = "Manual Review"

        aprendizados.append({
            "cnpj": cnpj,
            "produto": produto,
            "ncm": ncm,
            "cfop": cfop,
            "cst": cst,
            "estrategia_aprendida": estrategia_aprendida
        })

    if not aprendizados:
        print("[ERRO] Nenhum dado válido foi aprendido.")
        return

    print(f"✅ {len(aprendizados)} padrões aprendidos com sucesso.")
    for a in aprendizados:
        print(a)
