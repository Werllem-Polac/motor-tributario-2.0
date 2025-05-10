# ia_motor/treinador_estrategias.py

def treinar_ia(dados):
    try:
        if not isinstance(dados, list) or not dados:
            raise ValueError("Dados inválidos para treinamento")

        print(" Iniciando treinamento de IA com os dados...")

        # Simulação do processo de "treinamento"
        for d in dados:
            cnpj = d.get("cnpj", "desconhecido")
            print(f"📚 Treinando IA para CNPJ: {cnpj}")
            if isinstance(d, dict):
                cnpj = d.get("cnpj", "desconhecido")
                print(f"📚 Treinando IA para CNPJ: {cnpj}")
            else:
                print(f"[!] Registro inválido (não é dict): {d}")

        print(" Treinamento concluído com sucesso!")

    except Exception as e:
        print(f"[ERRO] Falha no treinamento da IA: {str(e)}")