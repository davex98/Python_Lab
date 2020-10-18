from unittest import TestCase
from MatrixMultiplication import matrixMultiplication


class Test(TestCase):
    def test_matrix_multiplication(self):
        # given
        m1 = [[-1, -2, 3],
              [0, 2, -1],
              [-1, 3, 0]]

        m2 = [[1, 5, 1],
              [2, 1, 2],
              [3, 2, 3]]

        # when
        m3 = matrixMultiplication(m1, m2)

        # then
        excpectedMatrix = [[4, -1, 4],
                           [1, 0, 1],
                           [5, -2, 5]]
        self.assertEqual(m3, excpectedMatrix)
