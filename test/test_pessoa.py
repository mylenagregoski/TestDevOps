import unittest
from pessoa import Pessoa

class TestPessoa(unittest.TestCase):
    def test_saudacao(self):
        pessoa = Pessoa("Ana", 30)
        self.assertEqual(pessoa.saudacao(), "Olá, meu nome é Ana e tenho 30 anos.")

    def test_atributos(self):
        pessoa = Pessoa("Carlos", 25)
        self.assertEqual(pessoa.nome, "Carlos")
        self.assertEqual(pessoa.idade, 25)

if __name__ == '__main__':
    unittest.main()
