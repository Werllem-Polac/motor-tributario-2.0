from sentence_transformers import SentenceTransformer
import numpy as np

modelo = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

def gerar_embedding(texto: str) -> np.ndarray:
    return modelo.encode(texto)

def similaridade(v1: np.ndarray, v2: np.ndarray) -> float:
    return float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
