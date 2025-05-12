"""
Rotas da API relacionadas à entidade Empresa.
Inclui criação e consulta por ID.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database.session import get_db
from api.empresas import services, schemas

router = APIRouter(prefix="/empresas", tags=["Empresas"])

@router.post("/", response_model=schemas.Empresa)
def criar_empresa(empresa: schemas.EmpresaCreate, db: Session = Depends(get_db)):
    """
    Cria uma nova empresa no banco de dados.

    Parâmetros:
    - empresa: dados da nova empresa no formato EmpresaCreate
    - db: instância do banco de dados via dependência

    Retorna:
    - Objeto da empresa criada
    """
    return services.criar_empresa(db, empresa)

@router.get("/{empresa_id}", response_model=schemas.Empresa)
def obter_empresa(empresa_id: int, db: Session = Depends(get_db)):
    """
    Retorna uma empresa pelo ID.

    Parâmetros:
    - empresa_id: identificador único da empresa
    - db: instância do banco de dados via dependência

    Exceções:
    - 404 se empresa não for encontrada

    Retorna:
    - Objeto da empresa
    """
    empresa = services.get_empresa_by_id(db, empresa_id)
    if not empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return empresa
