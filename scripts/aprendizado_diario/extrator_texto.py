def processar(documentos):
    """
    Faz o pré-processamento dos documentos jurídicos:
    limpeza básica e unificação de campos.
    """
    textos_processados = []
    for doc in documentos:
        texto_limpo = doc["texto"].replace("\n", " ").strip()
        textos_processados.append({
            "fonte": doc["fonte"],
            "titulo": doc["titulo"],
            "texto": texto_limpo
        })
    return textos_processados
