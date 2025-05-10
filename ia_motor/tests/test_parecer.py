import unittest
from ia_motor.services.gerador_defesa import gerar_defesa

class TestGeradorDefesa(unittest.TestCase):

    def test_contem_tese_e_cnpj(self):
        cnpj = "12345678000100"
        tese = "crédito presumido"
        parecer = gerar_defesa(tese, cnpj)
        self.assertIn(cnpj, parecer)
        self.assertIn(tese, parecer)
        self.assertIn("Modelo de Defesa Tributária", parecer)

