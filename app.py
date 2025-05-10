# app.py

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

from upload_files.upload_area import layout_upload, registrar_callbacks_upload

# Inicialização do aplicativo Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
server = app.server  # necessário para deploy

# Layout base
app.layout = html.Div([
    html.H1("📊 Motor Tributário Inteligente", className="text-center mt-3 mb-4"),

    dbc.Tabs([
        dbc.Tab(label="📁 Upload",        tab_id="upload"),
        dbc.Tab(label="📊 Relatórios",    tab_id="relatorios"),
        dbc.Tab(label="💬 Chat Tributário", tab_id="chat"),
    ], id="abas", active_tab="upload"),

    html.Div(id="conteudo"),
])

# Callback para troca de conteúdo nas abas
@app.callback(
    dash.Output("conteudo", "children"),
    dash.Input("abas", "active_tab")
)
def alternar_aba(tab):
    if tab == "upload":
        return layout_upload
    elif tab == "relatorios":
        return html.Div("📄 Relatórios em construção.")
    elif tab == "chat":
        return html.Div("🤖 Chat IA em desenvolvimento.")
    return html.Div("❓ Aba desconhecida.")

# Registrar callbacks adicionais
registrar_callbacks_upload(app)

if __name__ == "__main__":
    app.run(debug=True)
