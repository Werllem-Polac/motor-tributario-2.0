from fpdf import FPDF
import pandas as pd
import os

def gerar_pdf(dados: list):
    try:
        # Converte os dados para DataFrame
        df = pd.DataFrame(dados)

        # Evita erro: “valores escalares requerem índice”
        if df.empty:
            raise ValueError("O DataFrame está vazio. Nada a gerar.")

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt="Relatório Tributário", ln=True, align="C")
        pdf.ln(10)

        # Adiciona colunas como título
        colunas = df.columns.tolist()
        for col in colunas:
            pdf.cell(40, 10, txt=col, border=1)
        pdf.ln()

        # Adiciona linhas
        for _, row in df.iterrows():
            for col in colunas:
                pdf.cell(40, 10, txt=str(row[col])[:15], border=1)
            pdf.ln()

        os.makedirs("relatorios", exist_ok=True)
        pdf.output("relatorios/saida_analise.pdf")
        print("✅ Relatório PDF gerado com sucesso!")

    except Exception as e:
        print(f"[ERRO] Falha ao gerar o relatório: {str(e)}")
