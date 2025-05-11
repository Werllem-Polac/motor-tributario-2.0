class ClassificadorEmpresa:
    def __init__(self, cnae: str, regime: str, uf: str):
        self.cnae = cnae
        self.regime = regime
        self.uf = uf

    def classificar_tipo_empresa(self):
        if self.cnae.startswith("1"):
            return "Indústria"
        elif self.cnae.startswith("4") or self.cnae.startswith("5"):
            return "Comércio"
        elif self.cnae.startswith("6") or self.cnae.startswith("7") or self.cnae.startswith("8"):
            return "Serviço"
        else:
            return "Misto"

    def sugerir_teses(self):
        tipo = self.classificar_tipo_empresa()
        sugestoes = []

        if tipo == "Indústria":
            sugestoes = [
                "Tese da Essencialidade",
                "Energia Elétrica como insumo",
                "Crédito Presumido ICMS",
                "Redução de Base de Cálculo"
            ]
        elif tipo == "Comércio":
            sugestoes = [
                "Substituição Tributária Indevida",
                "Alíquota Inadequada por Regime",
                "Tese do Diferimento não aplicado"
            ]
        elif tipo == "Serviço":
            sugestoes = [
                "ISS fora da base do PIS/COFINS",
                "Lucro Arbitrado",
                "Simples Nacional – vedação indevida de crédito"
            ]
        else:
            sugestoes = [
                "Análise combinada – múltiplas atividades",
                "Análise do Fator R (Simples Nacional)",
                "Verificação cruzada de Regimes aplicáveis"
            ]

        return {
            "tipo_empresa": tipo,
            "teses_recomendadas": sugestoes
        }
