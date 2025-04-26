import unittest
from validador import email_valido

class TestValidador(unittest.TestCase):
    def test_email_valido(self):
        self.assertTrue(email_valido("teste@exemplo.com"))
        self.assertTrue(email_valido("usuario.name@dominio.co"))

    def test_email_invalido(self):
        self.assertFalse(email_valido("invalido"))
        self.assertFalse(email_valido("semarroba.com"))
        self.assertFalse(email_valido("user@.com"))

if __name__ == '__main__':
    unittest.main()
