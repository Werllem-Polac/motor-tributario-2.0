# dashboard/chat_layout.py
layout_chat = html.Div([
    dcc.Input(id="input-cnpj", placeholder="Digite o CNPJ..."),
    dcc.Textarea(id="input-pergunta", placeholder="Digite a pergunta..."),
    html.Button("Perguntar", id="botao-pergunta"),
    html.Div(id="resposta-chat")
])
