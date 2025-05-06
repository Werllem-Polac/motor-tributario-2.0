from fpdf import FPDF
from datetime import datetime
import os

# Função para gerar Relatório PDF Premium
def gerar_relatorio_pdf(df, empresa):
    # Nome do arquivo dinâmico
    timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M")
    nome_arquivo = f"relatorios/Relatorio_{empresa.replace(' ', '_')}_{timestamp}.pdf"

    # Criação do PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Header
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, f"Relatório Tributário - {empresa}", ln=True, align="C")

    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 10, f"Data de geração: {datetime.now().strftime('%d/%m/%Y %H:%M')}", ln=True, align="C")
    pdf.ln(10)

    # KPIs
    total_produtos = len(df)
    economia_total = df['Valor_Produto'].sum() * df['Economia_Percentual'].mean() / 100
    estrategias_aplicadas = df['Estrategia'].nunique()

    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Resumo de Indicadores:", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 8, f"Total de Produtos Analisados: {total_produtos}", ln=True)
    pdf.cell(0, 8, f"Economia Fiscal Estimada: R$ {economia_total:,.2f}", ln=True)
    pdf.cell(0, 8, f"Estrategias Aplicadas: {estrategias_aplicadas}", ln=True)
    pdf.ln(10)

    # Tabela de dados
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Tabela de Produtos Analisados:", ln=True)
    pdf.ln(5)
    pdf.set_font("Arial", '', 10)

    # Cabeçalho da Tabela
    colunas = ["Produto", "NCM", "CFOP", "Estrategia", "Valor Produto", "Economia (%)"]
    larguras = [40, 25, 20, 50, 25, 20]

    for i, coluna in enumerate(colunas):
        pdf.cell(larguras[i], 8, coluna, border=1, align="C")
    pdf.ln()

    # Dados da Tabela
    for index, row in df.iterrows():
        pdf.cell(larguras[0], 8, str(row['Produto'])[:20], border=1)
        pdf.cell(larguras[1], 8, str(row['NCM']), border=1)
        pdf.cell(larguras[2], 8, str(row['CFOP']), border=1)
        pdf.cell(larguras[3], 8, str(row['Estrategia'])[:28], border=1)
        pdf.cell(larguras[4], 8, f"R$ {row['Valor_Produto']:,.2f}", border=1)
        pdf.cell(larguras[5], 8, f"{row['Economia_Percentual']}%", border=1)
        pdf.ln()

    # Salvar PDF
    if not os.path.exists("relatorios"):
        os.makedirs("relatorios")

    pdf.output(nome_arquivo)

    return nome_arquivo