import unittest
import meupacote

class TestInit(unittest.TestCase):
    def test_saudacao_padrao(self):
        self.assertEqual(meupacote.saudacao("Mylena"), "Olá, Mylena!")

    def test_saudacao_vazia(self):
        self.assertEqual(meupacote.saudacao("Camila"), "Olá, Camila!")

    def test_saudacao_espaco(self):
        self.assertEqual(meupacote.saudacao("Eloá", "olá, Eloá!"))

if __name__ == '__main__':
    unittest.main()