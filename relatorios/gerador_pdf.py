from fpdf import FPDF
import os

def gerar_pdf(dados):
    if dados is None:
        print("[ERRO] Nenhum dado foi carregado para o Gerador de PDF.")
        return

    pasta_saida = "relatorios"
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    caminho_pdf = os.path.join(pasta_saida, "relatorio_estrategias.pdf")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Relatório de Estratégias Tributárias", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", '', 12)

    for index, nota in dados.iterrows():
        produto = nota['Produto']
        ncm = str(nota['NCM'])
        cfop = str(nota['CFOP'])
        cst = str(nota['CST'])

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

        pdf.cell(0, 10, f"Produto: {produto}", ln=True)
        if estrategias:
            for estrategia in estrategias:
                pdf.cell(0, 10, f" - {estrategia}", ln=True)
        else:
            pdf.cell(0, 10, "- Nenhuma estratégia clara", ln=True)
        pdf.ln(5)

    pdf.output(caminho_pdf)

    print(f"\n Relatório PDF gerado com sucesso em: {caminho_pdf}")