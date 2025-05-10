import unittest
from ia_motor.services.simulador_fiscal import simular_por_tese

class FakeEmpresa:
    cnpj = "12345678000100"
    nome = "Empresa Teste"
    uf = "SP"
    regime = "Lucro Real"

class DBFake:
    def query(self, model): return self
    def filter(self, cond): return self
    def first(self): return FakeEmpresa()

class TestSimuladorFiscal(unittest.TestCase):

    def test_simulacao_valida(self):
        db = DBFake()
        resultado = simular_por_tese("12345678000100", "crédito presumido", db)
        self.assertIn("economia", resultado)
        self.assertGreater(resultado["economia"], 0)
        self.assertEqual(resultado["tese"], "crédito presumido")

