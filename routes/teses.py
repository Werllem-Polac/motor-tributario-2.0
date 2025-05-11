from fastapi import APIRouter
from schemas.teses import RequisicaoClassificacao, ResultadoClassificacao
from services.classificador_empresa import ClassificadorEmpresa

router = APIRouter()

@router.post("/classificar/empresa", response_model=ResultadoClassificacao)
def classificar_empresa(dados: RequisicaoClassificacao):
    classificador = ClassificadorEmpresa(
        cnae=dados.cnae,
        regime=dados.regime_tributario,
        uf=dados.uf
    )
    resultado = classificador.sugerir_teses()
    return resultado
