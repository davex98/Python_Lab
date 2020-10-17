import math

from Classes.MyComplex import Complex


def quadraticEquation(a, b, c):
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))
    if dis > 0:
        r1 = (-b + sqrt_val) / (2 * a)
        r2 = (-b - sqrt_val) / (2 * a)
        return r1, r2
    elif dis == 0:
        return -b / (2 * a)
    else:
        r1 = Complex(- b / (2 * a), sqrt_val)
        r2 = Complex(- b / (2 * a), -sqrt_val)
        return r1, r2
