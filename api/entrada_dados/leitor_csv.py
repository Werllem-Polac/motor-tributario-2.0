import pandas as pd

def ler_arquivo_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        return {"erro": str(e)}
