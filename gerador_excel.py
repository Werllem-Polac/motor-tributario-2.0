import pandas as pd
from datetime import datetime
import os

# Função para gerar Relatório Excel Premium
def gerar_relatorio_excel(df, empresa):
    # Nome do arquivo dinâmico
    timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M")
    nome_arquivo = f"relatorios/Relatorio_{empresa.replace(' ', '_')}_{timestamp}.xlsx"

    # Se não existir a pasta de relatórios, criar
    if not os.path.exists("relatorios"):
        os.makedirs("relatorios")

    # Salvar DataFrame como Excel
    with pd.ExcelWriter(nome_arquivo, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name="Relatorio", index=False)

        # Formatar a Planilha
        workbook = writer.book
        worksheet = writer.sheets["Relatorio"]

        # Ajustar colunas
        for idx, col in enumerate(df.columns):
            largura = max(df[col].astype(str).map(len).max(), len(col)) + 2
            worksheet.set_column(idx, idx, largura)

        # Formatar cabeçalho
        header_format = workbook.add_format({
            'bold': True,
            'text_wrap': True,
            'valign': 'middle',
            'align': 'center',
            'border': 1,
            'bg_color': '#DCE6F1'
        })

        for col_num, value in enumerate(df.columns.values):
            worksheet.write(0, col_num, value, header_format)

    return nome_arquivo