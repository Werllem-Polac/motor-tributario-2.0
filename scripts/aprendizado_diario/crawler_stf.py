import requests
from bs4 import BeautifulSoup

def coletar():
    """
    Coleta jurisprudências recentes do STF (simulado para exemplo).
    """
    url = "https://www.stf.jus.br/portal/jurisprudencia/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    resultados = []
    for item in soup.select(".resultadoJurisprudencia"):
        titulo = item.select_one(".tituloJurisprudencia").text
        texto = item.select_one(".resumoJurisprudencia").text
        resultados.append({
            "fonte": "STF",
            "titulo": titulo.strip(),
            "texto": texto.strip()
        })

    return resultados
