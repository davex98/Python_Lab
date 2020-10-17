from math import sqrt


class Complex(object):
    def __init__(self, real, imag=0.0):
        self.real = int(real)
        self.imag = int(imag)

    def __add__(self, other):
        return Complex(self.real + other.real,
                       self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real,
                       self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.imag * other.real + self.real * other.imag)

    def __truediv__(self, other):
        conj = other.conjugate()

        den = other * conj
        den = den.real

        num = self * conj
        return Complex(num.real / den, num.imag / den)

    def __abs__(self):
        return sqrt(self.real ** 2 + self.imag ** 2)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return "{} + {}j".format(self.real, self.imag)

    def __repr__(self):
        return 'Complex' + str(self)

    def conjugate(self):
        return Complex(self.real, -self.imag)
