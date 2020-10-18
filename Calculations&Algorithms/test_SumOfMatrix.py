from unittest import TestCase
from SumOfMatrix import matrixSum
from SumOfMatrix import getRandomMatrix
import numpy as np

class Test(TestCase):
    def test_matrix_sum(self):
        # given
        a = [[1, 1],
             [1, 1]]

        b = [[1, 1],
             [1, 1]]

        # when
        c = matrixSum(a, b)
        # then
        self.assertEqual(c, [[2, 2], [2, 2]])

    def test_128_matrix(self):
        # given
        a = getRandomMatrix(128, 128)
        b = getRandomMatrix(128, 128)

        # when
        c = matrixSum(a, b)

        # then
        self.assertTrue(((np.matrix(c) == np.matrix(b) + np.matrix(a)).all()))
