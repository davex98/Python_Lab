from MyComplex import Complex
import unittest



class test_MyComplex(unittest.TestCase):
    def test_addTwoComplexNumbers(self):
        data = [[(2, 3), (3, 6), (5, 9)],
                [(-4, 7), (3, -9), (-1, -2)],
                [(0, 0), (0, 0), (0, 0)]]
        for a, b, c in data:
            # given
            n1 = Complex(a[0], a[1])
            n2 = Complex(b[0], b[1])

            # when
            n3 = n1 + n2

            # then
            self.assertEqual(n3.real, c[0])
            self.assertEqual(n3.imag, c[1])

    def test_subTwoComplexNumber(self):
        data = [[(2, 3), (3, 6), (-1, -3)],
                [(-4, 7), (3, -9), (-7, 16)],
                [(0, 0), (0, 0), (0, 0)]]
        for a, b, c in data:
            # given
            n1 = Complex(a[0], a[1])
            n2 = Complex(b[0], b[1])

            # when
            n3 = n1 - n2

            # then
            self.assertEqual(n3.real, c[0])
            self.assertEqual(n3.imag, c[1])

    def test_mulTwoComplexNumber(self):
        data = [[(5, 2), (3, -7), (29, -29)],
                [(4, 1), (7, -3), (31, -5)]]
        for a, b, c in data:
            # given
            n1 = Complex(a[0], a[1])
            n2 = Complex(b[0], b[1])

            # when
            n3 = n1 * n2

            # then
            self.assertEqual(n3.real, c[0])
            self.assertEqual(n3.imag, c[1])

    def test_divTwoComplexNumber(self):
        data = [[(4, -7), (-3, 2), (-2, 1)]]
        for a, b, c in data:
            # given
            n1 = Complex(a[0], a[1])
            n2 = Complex(b[0], b[1])

            # when
            n3 = n1 / n2

            # then
            self.assertEqual(n3.real, c[0])
            self.assertEqual(n3.imag, c[1])

    def test_absTwoComplexNumber(self):
        data = [[(3, 4), 5],
                [(0, 10), 10]]
        for a, b in data:
            # given
            n1 = Complex(a[0], a[1])

            # when
            n3 = n1.__abs__()

            # then
            self.assertEqual(n3, b)

if __name__ == '__main__':
    unittest.main()

