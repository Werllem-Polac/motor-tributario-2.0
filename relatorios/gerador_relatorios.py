import pandas as pd
import os

def gerar_relatorio(dados):
    print("\n📄 Iniciando geração do relatório tabular...")

    # Garantir que os dados estejam no formato de DataFrame
    if dados is None:
        print("[ERRO] Nenhum dado fornecido.")
        return

    if isinstance(dados, list):
        dados = pd.DataFrame(dados)
    elif isinstance(dados, dict):
        dados = pd.DataFrame([dados])
    elif not isinstance(dados, pd.DataFrame):
        print("[ERRO] Formato de dados não reconhecido.")
        return

    if dados.empty:
        print("[ERRO] Nenhum dado válido para relatório.")
        return

    # Verificar e preencher colunas esperadas
    colunas_esperadas = ["CNPJ", "Produto", "NCM", "CFOP", "CST"]

    for col in colunas_esperadas:
        if col not in dados.columns:
            print(f"[AVISO] Coluna ausente: {col}. Será preenchida com 'não informado'.")
            dados[col] = "não informado"

    # Reorganizar colunas para saída
    colunas_saida = [col for col in colunas_esperadas if col in dados.columns]

    # Criar diretório se necessário
    os.makedirs("relatorios", exist_ok=True)

    try:
        # Salvar relatório principal em CSV + Excel
        dados[colunas_saida].to_csv("relatorios/relatorio_geral.csv", index=False)
        dados[colunas_saida].to_excel("relatorios/relatorio_geral.xlsx", index=False)
        print("✅ Relatório tabular gerado com sucesso em: relatorios/relatorio_geral.*")
    except Exception as e:
        print(f"[ERRO] Falha ao gerar o relatório: {str(e)}")
