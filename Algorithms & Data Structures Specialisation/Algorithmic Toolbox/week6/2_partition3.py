# Uses python3
import sys
import itertools
import random


def partition3(A):
    total = sum(A)
    n = len(A)
    if total % 3 != 0:
        return 0

    total = total//3
    v = init_matrix3(total, total, n)
    for tot_1 in range(total+1):
        for tot_2 in range(total+1):
            for ai in range(n+1):
                if tot_1 == tot_2 == 0:
                    v[tot_1][tot_2][ai] = 1
                elif ai == 0 and (tot_1 != 0 or tot_2 != 0):
                    v[tot_1][tot_2][ai] = 0
                else:
                    a = A[ai-1]
                    if tot_1 >= a:
                        d11 = v[tot_1-a][tot_2][ai-1]
                        d12 = v[tot_1][tot_2][ai - 1]
                        d1 = max(d11, d12)
                    else:
                        d1 = v[tot_1][tot_2][ai-1]
                    if tot_2 >= a:
                        d21 = v[tot_1][tot_2-a][ai-1]
                        d22 = v[tot_1][tot_2][ai-1]
                        d2 = max(d21, d22)
                    else:
                        d2 = v[tot_1][tot_2][ai-1]
                    v[tot_1][tot_2][ai] = max(d1, d2)
    return v[total][total][n]


def partition2(A):
    total = sum(A)
    n = len(A)
    if total % 2 != 0:
        return 0
    else:
        total = total // 2
        v = init_matrix(total, n)
        for tot in range(total+1):
            for ai in range(n+1):
                if tot == 0:
                    v[tot][ai] = 1
                elif ai == 0 and tot != 0:
                    v[tot][ai] = 0
                else:
                    a = A[ai-1]
                    if tot >= a:
                        d1 = v[tot-a][ai-1]
                        d2 = v[tot][ai-1]
                        v[tot][ai] = max(d1, d2)
                    else:
                        v[tot][ai] = v[tot][ai-1]

    return v[total][n]


def init_matrix(n, m):
    matrix = []
    for i in range(n+1):
        l = []
        for j in range(m+1):
            l.append(0)
        matrix.append(l)
    return matrix


def init_matrix3(n1, n2, n3):
    matrix = []
    for i in range(n1+1):
        l = init_matrix(n2, n3)
        matrix.append(l)
    return matrix


def generate_array(total):
    size = random.randint(1, 5)
    sum = 0
    a = []
    for _ in range(size-1):
        new = random.randint(0, total-sum)
        sum += new
        a.append(new)
    a.append(total-sum)
    return a


def naive():
    total = random.randint(10, 100)
    l = []
    a = []
    for _ in range(3):
        k = generate_array(total)
        a.append(k)
        l += k
    return shuffle(l), a


def shuffle(l):
    for _ in range(10):
        i = random.randint(0, len(l)-1)
        l[i], l[1] = l[1], l[i]
    return l


if __name__ == '__main__':
    # A = [3, 3, 3, 3, 5, 58, 1, 48]
    # partition2(A)
    while True:
        A, a = naive()
        if partition3(A+[2, 1]) == 0:
            print("OK")
        else:
            print(A)
            print(a)
            break

    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

