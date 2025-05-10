from pydantic import BaseModel

class UsuarioCreateSchema(BaseModel):
    email: str
    senha: str

class UsuarioLoginSchema(BaseModel):
    email: str
    senha: str

class EmpresaSchema(BaseModel):
    nome: str
    cnpj: str

class ProdutoSchema(BaseModel):
    nome: str
    ncm: str
    empresa_id: int

class PerguntaIASchema(BaseModel):
    pergunta: str
    cnpj: str
