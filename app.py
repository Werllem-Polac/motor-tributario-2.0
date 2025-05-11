import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

# Layouts e callbacks do Dash
from upload_files.upload_area import layout_upload, registrar_callbacks_upload
from dashboard.layout_dashboard import layout_dashboard
from dashboard.callbacks_dashboard import registrar_callbacks_dashboard

# ==== FASTAPI IMPORTS ====
from fastapi import FastAPI
from routes.analise import router as analise_router
from routes.teses import router as teses_router
from routes.auditoria import router as auditoria_router

# ==== INSTÂNCIA FASTAPI ====
fastapi_app = FastAPI(
    title="Motor Tributário Inteligente - API",
    version="1.0.0",
)

# Rotas da API
fastapi_app.include_router(analise_router, prefix="/api", tags=["Análise Tributária"])
fastapi_app.include_router(teses_router, prefix="/api", tags=["Teses Inteligentes"])
fastapi_app.include_router(auditoria_router, prefix="/api", tags=["Auditoria Fiscal"])

# ==== DASH APP ====
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
    server=fastapi_app  # vincula ao backend FastAPI
)
server = app.server  # usado para deploy (ex: Railway)

# ==== LAYOUT BASE DO DASH ====
app.layout = html.Div([
    html.H1("📊 Motor Tributário Inteligente", className="text-center mt-3 mb-4"),

    dbc.Tabs([
        dbc.Tab(label="📁 Upload",         tab_id="upload"),
        dbc.Tab(label="📊 Relatórios",     tab_id="relatorios"),
        dbc.Tab(label="💬 Chat Tributário", tab_id="chat"),
    ], id="abas", active_tab="upload"),

    html.Div(id="conteudo"),
])

# ==== CALLBACK: Troca de abas ====
@app.callback(
    dash.Output("conteudo", "children"),
    dash.Input("abas", "active_tab")
)
def alternar_aba(tab):
    if tab == "upload":
        return layout_upload
    elif tab == "relatorios":
        return layout_dashboard()
    elif tab == "chat":
        return html.Div("🤖 Chat IA em desenvolvimento.")
    return html.Div("❓ Aba desconhecida.")

# ==== REGISTRO DE CALLBACKS EXTERNOS ====
registrar_callbacks_upload(app)
registrar_callbacks_dashboard(app)

# ==== EXECUÇÃO LOCAL ====
if __name__ == "__main__":
    app.run(debug=True)
