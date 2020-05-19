import unittest
import numpy as np
from operacoes import *


class OperacoesTestCase(unittest.TestCase):
    def test_exercicio_1(self):
        original = np.array([[10, 15, 15, 5, 5],
                             [20, 15, 5, 5, 15]])

        matrix_esperada = np.array([[15, 20, 20, 10, 10],
                                   [23, 18, 8, 8, 18]])

        transladada = translacao(original, 5, 3)

        self.assertTrue((matrix_esperada == transladada).all())

    def test_exercicio_2(self):
        original = np.array([[10, 15, 15, 5, 5],
                             [20, 15, 5, 5, 15]])

        matrix_esperada = np.array([[20, 30, 30, 10, 10],
                                   [60, 45, 15, 15, 45]])

        escalada = escala(original, 2, 3)

        self.assertTrue((matrix_esperada == escalada).all())


if __name__ == '__main__':
    unittest.main()
