import unittest
from ia_motor.services.classificador_risco import calcular_risco

class TestClassificadorRisco(unittest.TestCase):

    def test_risco_alto(self):
        dados = {"valor_total": "150000"}
        risco = calcular_risco("12345678000100", dados)
        self.assertGreaterEqual(risco, 0.8)

    def test_risco_medio(self):
        dados = {"valor_total": "60000"}
        risco = calcular_risco("12345678000100", dados)
        self.assertGreaterEqual(risco, 0.5)

    def test_risco_baixo(self):
        dados = {"valor_total": "5000"}
        risco = calcular_risco("12345678000100", dados)
        self.assertLessEqual(risco, 0.2)

