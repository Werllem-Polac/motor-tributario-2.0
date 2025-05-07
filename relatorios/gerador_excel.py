import pandas as pd

def gerar_excel(dados: list):
    try:
        # Converte lista de dicionários em DataFrame
        df = pd.DataFrame(dados)

        # Caminho de saída
        df.to_excel("relatorios/saida_analise.xlsx", index=False)
        print(" Relatório Excel gerado com sucesso!")
    except Exception as e:
        print(f"[ERRO] Falha ao gerar o relatório: {str(e)}")
