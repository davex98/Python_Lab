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

if __name__ == '__main__':
    unittest.main()