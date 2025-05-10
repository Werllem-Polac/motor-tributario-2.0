def gerar_teses_por_ncm(ncm: str, uf: str) -> list:
    return [
        f"Tese alternativa baseada na NCM {ncm} válida para a UF {uf}",
        f"Isenção parcial de ICMS para NCM {ncm} sob análise de essencialidade",
        f"Diferimento fiscal aplicável a {ncm} com base na cadeia produtiva em {uf}"
    ]

