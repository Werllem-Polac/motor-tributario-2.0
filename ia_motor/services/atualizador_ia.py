from app.api.database.utils import get_empresa_by_cnpj  # ajuste o caminho conforme onde estiver o utils.py

def simular_por_tese(cnpj: str, tese: str, db):
    empresa = get_empresa_by_cnpj(db, cnpj)
    if not empresa:
        return {"erro": "Empresa não encontrada"}

    # Base simulada – em produção usar dados reais
    fatores = {
        "desoneração insumos": 0.05,
        "crédito presumido": 0.08,
        "tese da essencialidade": 0.10
    }

    fator = fatores.get(tese.lower(), 0.03)  # usa default de 3% se tese não mapeada
    economia = 500_000 * fator

    return {
        "cnpj": cnpj,
        "tese": tese,
        "economia": round(economia, 2),
        "regime": empresa.regime,
        "uf": empresa.uf
    }



