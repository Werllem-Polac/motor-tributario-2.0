def analisar_notas(lista):
    for item in lista:
        if isinstance(item, str):
            try:
                import json
                nota = json.loads(item)  # caso venha como string JSON
            except:
                continue  # ignora entradas inválidas
        elif isinstance(item, dict):
            nota = item
        else:
            continue

        if nota.get("valor", 0) > 1000:
            print(f"Nota relevante: {nota}")
