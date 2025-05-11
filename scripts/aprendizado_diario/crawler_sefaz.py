def coletar():
    """
    Coleta dados simulados da SEFAZ. Em produção, use crawler real por estado.
    """
    return [
        {
            "fonte": "SEFAZ-SP",
            "titulo": "Alteração de benefício fiscal",
            "texto": "A SEFAZ-SP publicou alteração no regulamento do ICMS..."
        },
        {
            "fonte": "SEFAZ-MG",
            "titulo": "Crédito presumido para frigoríficos",
            "texto": "Nova regra sobre crédito presumido de ICMS para abatedouros e frigoríficos..."
        }
    ]
