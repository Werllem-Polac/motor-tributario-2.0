import numpy as np

# Simula uma base vetorial com jurisprudência embutida
base_jurisprudencia = {
    "crédito presumido": np.array([0.1, 0.2, 0.3]),
    "tese da essencialidade": np.array([0.4, 0.5, 0.6]),
    "desoneração de insumos": np.array([0.7, 0.8, 0.9])
}

def vetorizar(texto: str) -> np.ndarray:
    # Em produção, usar um modelo como BERT ou OpenAI embeddings
    return np.random.rand(3)

def buscar_similaridade(vetor: np.ndarray) -> str:
    similaridades = {
        k: np.dot(v, vetor) for k, v in base_jurisprudencia.items()
    }
    return max(similaridades.items(), key=lambda item: item[1])[0]

