#Uses python3

import sys
import random

def lcs2(a, b):
    an = len(a)
    bn = len(b)

    x = init_matrix(an, bn)

    for i in range(an+1):
        for j in range(bn+1):
            if i == 0 or j == 0:
                x[i][j] = 0
            else:
                diff = 1 if a[i-1] == b[j-1] else 0
                x[i][j] = max(x[i][j-1], x[i-1][j], x[i-1][j-1]+diff)
    return x[an][bn]


def init_matrix(n, m):
    matrix = []
    for i in range(n+1):
        l = []
        for j in range(m+1):
            l.append(0)
        matrix.append(l)
    return matrix


def naive():
    n = random.randint(1, 4)
    a = []
    b = []
    for _ in range(n):
        x = random.randint(0, 20)
        a.append(x)
        b.append(x)
    a = randomize(a, 8)
    b = randomize(b, 9)
    return a, b, n


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
    # while True:
    #
    #     a, b, n = naive()
    #     if lcs2(a, b) == n:
    #         print("OK")
    #     else:
    #         print(a,b, n)
    #         break

    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))

