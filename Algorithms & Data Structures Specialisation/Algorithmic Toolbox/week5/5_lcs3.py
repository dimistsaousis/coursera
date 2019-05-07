#Uses python3
import random

import sys


def lcs3(a, b, c):
    an = len(a)
    bn = len(b)
    cn = len(c)
    x = init_matrix3d(an, bn, cn)

    for i in range(an+1):
        for j in range(bn+1):
            for k in range(cn+1):
                if i == 0 or j == 0 or k == 0:
                    x[i][j][k] = 0
                else:
                    diff = 1 if a[i-1] == b[j-1] == c[k-1] else 0
                    x[i][j][k] = max(x[i-1][j][k],
                                     x[i-1][j-1][k],
                                     x[i-1][j][k-1],
                                     x[i][j-1][k],
                                     x[i][j-1][k-1],
                                     x[i][j][k-1],
                                     x[i-1][j-1][k-1]+diff)

    return x[an][bn][cn]


def init_matrix(n, m):
    matrix = []
    for i in range(n+1):
        l = []
        for j in range(m+1):
            l.append(0)
        matrix.append(l)
    return matrix


def init_matrix3d(n1, n2, n3):
    matrix1 = []
    for i in range(n1+1):
        matrix2 = []
        for j in range(n2+1):
            matrix3 = []
            for k in range(n3+1):
                matrix3.append(0)
            matrix2.append(matrix3)
        matrix1.append(matrix2)
    return matrix1


def naive():
    n = random.randint(1, 10)
    a = []
    b = []
    c = []
    for _ in range(n):
        x = random.randint(0, 6)
        a.append(x)
        b.append(x)
        c.append(x)
    a = randomize(a, 7)
    b = randomize(b, 8)
    c = randomize(c, 9)
    return a, b, c, n


def randomize(a, id):
    size = random.randint(0, 10)
    for _ in range(size):
        i = random.randint(0, len(a)-1)
        x1 = a[:i]
        x2 = [id]
        x3 = a[i:]
        a = x1 + x2 + x3
    return a


if __name__ == '__main__':
    # a = [8, 3, 2, 1, 7]
    # b = [8, 2, 1, 3, 8, 10, 7]
    # c = [6, 8, 3, 1, 4, 7]
    # while True:
    #     a, b, c, n = naive()
    #     if lcs3(a, b, c) == n:
    #         print("OK")
    #     else:
    #         print(a,b,c, n)
    #         break
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
