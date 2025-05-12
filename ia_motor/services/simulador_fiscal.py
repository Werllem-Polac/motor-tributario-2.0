from app.api.database.utils import get_empresa_by_cnpj  # ajuste conforme a localização real do utils.py

def simular_por_tese(cnpj: str, tese: str, db):
    empresa = get_empresa_by_cnpj(db, cnpj)
    if not empresa:
        return {"erro": "Empresa não encontrada"}

    # Tabela de fatores simulados por tese
    fatores = {
        "desoneração insumos": 0.05,
        "crédito presumido": 0.08,
        "tese da essencialidade": 0.10
    }

    # Usa 0.03 como padrão se a tese não estiver mapeada
    fator = fatores.get(tese.lower(), 0.03)
    economia = 500_000 * fator

    return {
        "cnpj": cnpj,
        "tese": tese,
        "economia": round(economia, 2),
        "regime": empresa.regime,
        "uf": empresa.uf
    }
