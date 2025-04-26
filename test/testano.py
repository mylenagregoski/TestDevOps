import unittest
import meupacote

class TestAnoBissexto(unittest.TestCase):

    def test_ano_bissexto(self):
        self.assertTrue(meupacote.eh_bissexto(2024))

    def test_ano_nao_bissexto(self):
        self.assertFalse(meupacote.eh_bissexto(2023))

    def test_ano_secular_no_bissexto(self):
        self.assertFalse(meupacote.eh_bissexto(1900))

if __name__ == "__main__":
    unittest.main()