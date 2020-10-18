import random


def randomNumber():
    return random.randint(0, 99)


def getRandomMatrix():
    size = randomNumber()
    return [[randomNumber() for i in range(size)] for j in range(size)]


def getMatrixDeterminant(A):
    n = len(A)
    AM = A.copy()

    for fd in range(n):
        for i in range(fd + 1, n):
            crScaler = AM[i][fd] / AM[fd][fd]
            for j in range(n):
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]

    product = 1.0
    for i in range(n):
        product *= AM[i][i]

    return product


if __name__ == '__main__':
    a = getRandomMatrix()
    d = getMatrixDeterminant(a)
    print(d)
