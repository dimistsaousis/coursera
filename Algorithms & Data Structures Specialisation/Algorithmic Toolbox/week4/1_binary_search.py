# Uses python3
import sys


def binary_search(a, x, start=0):
    n = len(a)
    idx = n // 2

    if n == 0:
        return -1

    if a[idx] == x:
        return start+idx
    if a[idx] < x:
        return binary_search(a[idx+1:], x, idx+1+start)
    if a[idx] > x:
        return binary_search(a[:idx], x, start)


def binary_search2(a, x, low, high):
    while low <= high:
        mid = (high+low)//2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            low = mid+1
        else:
            high = mid-1

    return -1


def binary_search3(a, x, low, high):
    if low > high:
        return -1
    mid = (high+low)//2
    if a[mid] == x:
        return mid
    elif a[mid] < x:
        low = mid+1
    else:
        high = mid-1

    return binary_search3(a, x, low, high)


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    # import random
    #
    # while True:
    #     size = random.randint(2, 10)
    #     a = []
    #     x = random.randint(0, 100)
    #     for _ in range(size):
    #         a.append(random.randint(0, 10))
    #     a = sorted(set(a))
    #     print(a)
    #     print(x)
    #     if binary_search(a, x) != binary(a, x, 0, len(a)-1):
    #         print('FAILING')
    #         break
    #     else:
    #         print("OK")
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1:n + 1]
    for x in data[n + 2:]:
        print(binary_search2(a, x, 0, n-1), end=' ')
