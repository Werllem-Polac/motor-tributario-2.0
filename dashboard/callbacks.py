# dentro de app.py ou separado
@app.callback(
    dash.Output("resposta-chat", "children"),
    dash.Input("botao-pergunta", "n_clicks"),
    dash.State("input-cnpj", "value"),
    dash.State("input-pergunta", "value")
)
def chamar_chat(n, cnpj, pergunta):
    if not cnpj or not pergunta:
        return "Preencha CNPJ e pergunta."
    try:
        import requests
        r = requests.get(f"http://localhost:8000/chat/perguntar", params={"cnpj": cnpj, "pergunta": pergunta})
        return r.json().get("resposta", "Sem resposta.")
    except:
        return "Erro ao conectar à API."
