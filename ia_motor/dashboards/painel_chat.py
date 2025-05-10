import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = dbc.Container([
    html.H2("💬 Chat Tributário Inteligente"),
    dbc.Input(id="input_cnpj", placeholder="Digite o CNPJ", type="text"),
    dbc.Textarea(id="input_pergunta", placeholder="Digite sua pergunta tributária", style={"height": "120px"}),
    html.Br(),
    dbc.Button("Perguntar", id="btn-perguntar", color="success"),
    html.Br(), html.Br(),
    html.Div(id="resposta_chat")
])

@app.callback(
    Output("resposta_chat", "children"),
    Input("btn-perguntar", "n_clicks"),
    State("input_cnpj", "value"),
    State("input_pergunta", "value")
)
def responder(n, cnpj, pergunta):
    if not cnpj or not pergunta:
        return "❌ CNPJ e pergunta obrigatórios."
    return f"🤖 Resposta simulada para o CNPJ {cnpj}: '{pergunta}' será respondida com base jurídica."

if __name__ == "__main__":
    app.run(debug=True)

