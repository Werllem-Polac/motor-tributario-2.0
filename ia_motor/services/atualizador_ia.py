from ia_motor.database.utils import get_empresa_by_cnpj
import random

def simular_por_tese(cnpj: str, tese: str, db):
    empresa = get_empresa_by_cnpj(db, cnpj)
    if not empresa:
        return {"erro": "Empresa não encontrada"}

    # Base simulada (em produção, usar dados reais)
    fator = {
        "desoneração insumos": 0.05,
        "crédito presumido": 0.08,
        "tese da essencialidade": 0.1
    }.get(tese, 0.03)

    economia = 500000 * fator
    return {
        "cnpj": cnpj,
        "tese": tese,
        "economia": round(economia, 2),
        "regime": empresa.regime,
        "uf": empresa.uf
    }


