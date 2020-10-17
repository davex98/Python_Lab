from unittest import TestCase
from QuadraticEquation import quadraticEquation

from Classes.MyComplex import Complex


class Test(TestCase):
    def test_quadratic_equation_first(self):
        a = quadraticEquation(1, 2, 1)
        self.assertEqual(a, -1)

    def test_quadratic_equation_second(self):
        a = quadraticEquation(2, 2, 1)
        self.assertEqual(a[0], Complex(-0.5, 2))
        self.assertEqual(a[1], Complex(-0.5, -2))

    def test_quadratic_equation_third(self):
        a = quadraticEquation(1, 10, -24)
        self.assertEqual(a[0], 2)
        self.assertEqual(a[1], -12)
