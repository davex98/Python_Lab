from unittest import TestCase
from MatrixDeterminant import getMatrixDeterminant
import numpy as np

class Test(TestCase):
    def test_get_matrix_determinant(self):
        # given
        a = [[1, 2], [3, 4]]
        # when
        d = getMatrixDeterminant(a)
        # then
        self.assertEqual(d, int(np.linalg.det(a)))