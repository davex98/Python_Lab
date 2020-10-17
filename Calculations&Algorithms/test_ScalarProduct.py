from unittest import TestCase
from ScalarProduct import calculateScalarProduct


class Test(TestCase):
    def test_calculate_scalar_product(self):
        # given
        v1 = [1, 2, 12, 4]
        v2 = [2, 4, 2, 8]
        # when
        a = calculateScalarProduct(v1, v2)
        # then
        self.assertEqual(a, 66)
