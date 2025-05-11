from sentence_transformers import SentenceTransformer

modelo = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

def gerar(textos):
    """
    Gera embeddings para os textos jurídicos tratados.
    """
    vetores = []
    for doc in textos:
        embedding = modelo.encode(doc["texto"])
        vetores.append({
            "fonte": doc["fonte"],
            "titulo": doc["titulo"],
            "vetor": embedding
        })
    return vetores

