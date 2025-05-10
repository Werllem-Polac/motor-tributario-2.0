from pydantic import BaseModel
from pydantic.config import ConfigDict  # Novo para Pydantic v2

# ==========================
# MODELOS Pydantic (Schema)
# ==========================

class EmpresaSchema(BaseModel):
    id: int
    razao_social: str
    cnpj: str
    email: str
    telefone: str

    model_config = ConfigDict(from_attributes=True)


class DocumentoSchema(BaseModel):
    id: int
    empresa_id: int
    nome_arquivo: str
    data_envio: str

    model_config = ConfigDict(from_attributes=True)


class AnaliseSchema(BaseModel):
    id: int
    empresa_id: int
    tipo: str
    resultado: str
    data_analise: str

    model_config = ConfigDict(from_attributes=True)


class JurisprudenciaSchema(BaseModel):
    id: int
    titulo: str
    orgao: str
    ementa: str
    link: str

    model_config = ConfigDict(from_attributes=True)
