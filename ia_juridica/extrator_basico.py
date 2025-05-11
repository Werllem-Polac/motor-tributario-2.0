import re
import dateparser

def extrair_entidades(texto: str):
    """
    Extrai entidades jurídicas básicas com regex e análise de data.
    """
    cnpjs = re.findall(r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}', texto)
    valores = re.findall(r'R\$\s?\d{1,3}(?:\.\d{3})*,\d{2}', texto)
    artigos = re.findall(r'(art(?:igo)?\.?\s?\d+[A-Za-z]?)', texto, re.IGNORECASE)
    datas = [match.group() for match in re.finditer(r'\d{1,2}/\d{1,2}/\d{2,4}', texto)]

    try:
        from dateparser.search import search_dates
        datas_nat = search_dates(texto, languages=["pt"])
        if datas_nat:
            datas.extend([dt[0] for dt in datas_nat])
    except:
        pass

    return {
        "cnpjs": list(set(cnpjs)),
        "valores": list(set(valores)),
        "artigos": list(set(artigos)),
        "datas": list(set(datas))
    }
