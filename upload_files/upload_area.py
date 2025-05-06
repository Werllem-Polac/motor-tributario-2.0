import os, base64, pandas as pd, xml.etree.ElementTree as ET, requests
import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc

PASTA_UPLOAD = "base_dados/uploads_temp/"
os.makedirs(PASTA_UPLOAD, exist_ok=True)

layout_upload = dbc.Container([
    dbc.Row([dbc.Col(dcc.Upload(
        id="upload-data",
        children=html.Div(["Arraste e solte ou clique para selecionar"]),
        style={"width":"100%","height":"60px","lineHeight":"60px",
               "borderWidth":"1px","borderStyle":"dashed","textAlign":"center"},
        multiple=False
    ))]),
    html.Div(id="output-upload")
], fluid=True)

def salvar_arquivo(conteudo, nome):
    data = conteudo.encode("utf8").split(b";base64,")[1]
    caminho = os.path.join(PASTA_UPLOAD, nome)
    with open(caminho, "wb") as fp:
        fp.write(base64.decodebytes(data))
    return caminho

def interpretar_arquivo(caminho):
    ext = os.path.splitext(caminho)[1].lower()
    if ext == ".csv":
        df = pd.read_csv(caminho); return df.head().to_dict()
    if ext in [".xls", ".xlsx"]:
        df = pd.read_excel(caminho); return df.head().to_dict()
    if ext == ".xml":
        tree = ET.parse(caminho); return {"root": tree.getroot().tag}
    return {"erro": "Formato não suportado"}

def registrar_callbacks_upload(app):
    @app.callback(
        Output("output-upload","children"),
        Input("upload-data","contents"),
        State("upload-data","filename"),
        State("auth-token","data"),
        prevent_initial_call=True
    )
    def atualizar_output(conteudo, nome, token):
        caminho = salvar_arquivo(conteudo, nome)
        dados = interpretar_arquivo(caminho)
        headers = {"Authorization": f"Bearer {token}"} if token else {}
        try:
            r = requests.post(
                "http://127.0.0.1:8000/arquivos/",
                params={"nome": nome},
                headers=headers, timeout=5
            )
            if r.status_code == 200:
                msg = f"✅ '{r.json()['nome']}' registrado!"
            else:
                msg = f"❌ Erro API: {r.status_code}"
        except Exception as e:
            msg = f"❌ Falha API: {e}"
        return [html.Div(f"Dados extraídos: {dados}"), html.Div(msg)]
