# Uses python3
import sys
import random


def partition3(a, low, high):
    x = a[low]
    m1 = low

    # Strictly smaller
    for i in range(low+1, high+1):
        if a[i] < x:
            m1 += 1
            a[i], a[m1] = a[m1], a[i]
    a[low], a[m1] = a[m1], a[low]

    m2 = m1

    for i in range(m1+1, high+1):
        if a[i] == x:
            m2 += 1
            a[i], a[m2] = a[m2], a[i]

    return m1, m2


def partition2(a, low, high):
    x = a[low]
    pivot_index = low
    for i in range(low + 1, high + 1):
        if a[i] <= x:
            pivot_index += 1
            a[i], a[pivot_index] = a[pivot_index], a[i]
    a[low], a[pivot_index] = a[pivot_index], a[low]
    return pivot_index


def randomized_quick_sort(a, l, r):
    if l >= r:
        return a
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition3(a, l, r)
    # m = partition2(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)


if __name__ == '__main__':
    # while True:
    #     size = random.randint(5,100)
    #     a = []
    #     for _ in range(size):
    #         a.append(random.randint(0, 50))
    #     randomized_quick_sort(a, 0, len(a)-1)
    #     if a != sorted(a):
    #         print('WRONG')
    #         break
    #     else:
    #         print('OK')
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
