from pydantic import BaseModel

# --- Schemas para usuários ---
class UsuarioCreateSchema(BaseModel):
    email: str
    senha: str
    aceite_lgpd: bool

class UsuarioLoginSchema(BaseModel):
    email: str
    senha: str

class UsuarioSchema(BaseModel):
    id: int
    email: str

    class Config:
        orm_mode = True

# --- Schemas para empresas e produtos ---
class EmpresaSchema(BaseModel):
    nome: str
    cnpj: str

class ProdutoSchema(BaseModel):
    nome: str
    ncm: str
    empresa_id: int

# --- Schema para perguntas da IA ---
class PerguntaIASchema(BaseModel):
    pergunta: str
    cnpj: str