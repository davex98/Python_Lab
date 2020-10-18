import random


def matrixSum(X, Y):
    return [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]


def randomNumber():
    return random.randint(0, 99)


def getRandomMatrix(x, y):
    return [[randomNumber() for i in range(x)] for j in range(y)]