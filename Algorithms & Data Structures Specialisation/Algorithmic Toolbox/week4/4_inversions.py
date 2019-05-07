# Uses python3
import sys
import random


def merge_sort(a, left, right, inversions=0):
    if left == right:
        return a[left], inversions

    m = (left+right)//2

    b, inversions = merge_sort(a, left, m, inversions)
    c, inversions = merge_sort(a, m+1, right, inversions)
    return merge(b, c, inversions)


def merge(b, c, inversions):
    res = []
    b = b if isinstance(b, list) else [b]
    c = c if isinstance(c, list) else [c]
    while b and c:
        if b[0] <= c[0]:
            res.append(b[0])
            b.pop(0)
        else:
            res.append(c[0])
            c.pop(0)
            inversions += len(b)
    if b:
        res += b
    if c:
        res += c
    return res, inversions


def naive(a):
    n = len(a)
    inversions = 0
    for i in range(n):
        for j in range(i, n):
            if a[i] > a[j]:
                inversions += 1
    return inversions


if __name__ == '__main__':
    # while True:
    #     n = random.randint(2,5)
    #     a = []
    #     for _ in range(n):
    #         a.append(random.randint(0,10))
    #
    #     print("OK")
    #     if naive(a) != merge_sort(a, 0, len(a)-1)[1]:
    #         print(a)
    #         print("WRONG")
    #         break
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(merge_sort(a, 0, len(a)-1)[1])
