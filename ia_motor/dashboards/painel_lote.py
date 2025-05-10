import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = dbc.Container([
    html.H2("📂 Análise em Massa de CNPJs"),
    dcc.Textarea(id="lista_cnpjs", placeholder="Cole aqui os CNPJs separados por vírgula", style={"width": "100%", "height": "120px"}),
    html.Br(),
    dbc.Button("Analisar", id="btn-analisar", color="primary"),
    html.Br(), html.Br(),
    html.Div(id="resultado_lote")
])

@app.callback(
    Output("resultado_lote", "children"),
    Input("btn-analisar", "n_clicks"),
    State("lista_cnpjs", "value")
)
def executar_lote(n, texto):
    if not texto:
        return "❌ Por favor, informe os CNPJs."
    cnpjs = [c.strip() for c in texto.split(",") if c.strip()]
    return html.Ul([html.Li(f"{cnpj} → Simulação executada com sucesso") for cnpj in cnpjs])

if __name__ == "__main__":
    app.run(debug=True)



