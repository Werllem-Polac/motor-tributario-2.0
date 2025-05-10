import unittest
from ia_motor.chatbot.chat_core import responder_com_contexto

class EmpresaFake:
    cnpj = "12345678000100"
    nome = "Empresa Simulada"
    uf = "SP"
    regime = "Lucro Real"

class DBFake:
    def query(self, model): return self
    def filter(self, cond): return self
    def first(self): return EmpresaFake()

class TestChatTributario(unittest.TestCase):

    def test_resposta_ia(self):
        db = DBFake()
        pergunta = "Tenho direito ao crédito presumido?"
        resposta = responder_com_contexto("12345678000100", pergunta, db)
        self.assertIn("crédito presumido", resposta)
        self.assertIn("Fonte", resposta)

