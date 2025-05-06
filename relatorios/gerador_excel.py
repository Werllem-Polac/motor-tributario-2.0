import pandas as pd
import os

def gerar_excel(dados):
    if dados is None:
        print("[ERRO] Nenhum dado foi carregado para o Gerador de Excel.")
        return

    pasta_saida = "relatorios"
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    caminho_excel = os.path.join(pasta_saida, "relatorio_estrategias.xlsx")

    relatorio = []

    for index, nota in dados.iterrows():
        produto = nota['Produto']
        ncm = str(nota['NCM'])
        cfop = str(nota['CFOP'])
        cst = str(nota['CST'])
        valor_produto = float(nota['Valor_Produto'])

        estrategias = []

        if ncm.startswith('02'):
            estrategias.append("Tese da Desossa + Essencialidade")

        if ncm.startswith('05') or 'Ossos' in produto or 'Sebos' in produto:
            estrategias.append("Imunidade Agropecuária (Subprodutos)")

        if ncm.startswith('23'):
            estrategias.append("Regime Especial para Ração Animal (Isenção PIS/COFINS)")

        if cfop == '5102':
            estrategias.append("Crédito Presumido ICMS (Operação Interna)")

        if cst.startswith('0') or cst.startswith('1'):
            estrategias.append("Crédito Integral de ICMS")

        relatorio.append({
            "Produto": produto,
            "NCM": ncm,
            "CFOP": cfop,
            "CST": cst,
            "Valor Produto": valor_produto,
            "Estratégias Sugeridas": ", ".join(estrategias) if estrategias else "Nenhuma estratégia clara"
        })

    df_relatorio = pd.DataFrame(relatorio)
    df_relatorio.to_excel(caminho_excel, index=False)

    print(f"\n Relatório Excel gerado com sucesso em: {caminho_excel}")