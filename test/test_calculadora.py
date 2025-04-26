import unittest
from calculadora import soma, subtrai

class TestCalculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(-1, 1), 0)

    def test_subtrai(self):
        self.assertEqual(subtrai(5, 3), 2)
        self.assertEqual(subtrai(0, 4), -4)

if __name__ == '__main__':
    unittest.main()
