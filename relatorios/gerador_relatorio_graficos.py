from fpdf import FPDF
import os

def gerar_relatorio_graficos():
    print("\n Iniciando geração do Relatório Gráfico em PDF...")

    # Pasta onde os gráficos foram salvos
    pasta_graficos = "graficos"
    pasta_relatorios = "relatorios"

    # Arquivo PDF final
    caminho_pdf = os.path.join(pasta_relatorios, "relatorio_graficos.pdf")

    # Lista dos gráficos (agora SEM emojis!)
    graficos = [
        ("Estrategias Aplicadas por Produto", "estrategias_por_produto.png"),
        ("Economia Simulada por Estrategia", "economia_por_estrategia.png"),
        ("Comparativo de Tributos: Atual vs Otimizado", "comparativo_tributos.png"),
        ("Top 10 Produtos que Mais Economizam", "top10_produtos_economia.png"),
        ("Estrategias que Mais Impactam na Economia", "impacto_estrategias.png"),
        ("Produtos sem Estrategia Clara", "produtos_sem_estrategia.png"),
        ("Operacoes Internas vs Interestaduais", "cfop_interno_interestadual.png")
    ]

    # Criar o PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Capa
    pdf.add_page()
    pdf.set_font("Arial", 'B', 20)
    pdf.cell(0, 10, "Relatorio Grafico - Motor Tributario Inteligente", ln=True, align="C")
    pdf.ln(10)
    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 10, "Analises Estrategicas e Economicas Fiscais", ln=True, align="C")
    pdf.ln(20)

    # Inserir cada gráfico
    for titulo, arquivo in graficos:
        caminho_arquivo = os.path.join(pasta_graficos, arquivo)
        if os.path.exists(caminho_arquivo):
            pdf.add_page()
            pdf.set_font("Arial", 'B', 16)
            pdf.cell(0, 10, titulo, ln=True, align="C")
            pdf.ln(10)
            pdf.image(caminho_arquivo, w=180)  # Ajuste automático da largura da imagem
        else:
            print(f"[AVISO] Arquivo de gráfico não encontrado: {arquivo}")

    # Salvar o PDF
    pdf.output(caminho_pdf)

    print(f"\n Relatório Gráfico em PDF gerado com sucesso: {caminho_pdf}")