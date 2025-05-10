import pandas as pd
import os

def ler_arquivo_csv(file_path):
    if not os.path.exists(file_path):
        print(f"[ERRO] Arquivo não encontrado: {file_path}")
        return None

    try:
        df = pd.read_csv(file_path)
        if df.empty:
            print("[ERRO] O arquivo está vazio.")
            return None

        print(f"✅ CSV carregado com {df.shape[0]} linhas e {df.shape[1]} colunas.")
        return df

    except pd.errors.ParserError:
        print("[ERRO] Falha ao interpretar o CSV. Verifique o separador ou o conteúdo.")
    except Exception as e:
        print(f"[ERRO] Erro ao carregar o CSV: {str(e)}")

    return None

