from unittest import TestCase
from QuadraticEquation import quadraticEquation

from Classes.MyComplex import Complex


class Test(TestCase):
    def test_quadratic_equation_first(self):
        # given
        num = [1, 2, 1]
        # when
        a = quadraticEquation(*num)
        # them
        self.assertEqual(a, -1)

    def test_quadratic_equation_second(self):
        # given
        num = [2, 2, 1]
        # when
        a = quadraticEquation(*num)
        # them
        self.assertEqual(a[0], Complex(-0.5, 2))
        self.assertEqual(a[1], Complex(-0.5, -2))

    def test_quadratic_equation_third(self):
        # given
        num = [1, 10, -24]
        # when
        a = quadraticEquation(*num)
        # them
        self.assertEqual(a[0], 2)
        self.assertEqual(a[1], -12)
