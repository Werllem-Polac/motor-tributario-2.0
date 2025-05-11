import datetime

def registrar_resultado(resultado: dict):
    with open("ia_juridica/resultados.log", "a", encoding="utf-8") as f:
        f.write(f"\n[{datetime.datetime.now()}]\n")
        f.write(str(resultado))
        f.write("\n" + "-"*80 + "\n")
