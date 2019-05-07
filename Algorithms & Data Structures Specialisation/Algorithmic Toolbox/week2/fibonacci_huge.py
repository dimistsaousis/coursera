# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def calc_fib(n):
    l = [0, 1]
    if n <= 1:
        return n
    for i in range(2, n+1):
        l.append(l[i-1] + l[i-2])
    return l[-1]


def get_fibonacci_huge_algo(n, m):
    if m == 1:
        return calc_fib(n)
    if n <= 1:
        return n
    cycle = [0, 1]
    start = False
    while (cycle[-2], cycle[-1]) != (0, 1) or not start:
        start = True
        cycle.append((cycle[-2]+cycle[-1]) % m)
    cycle = cycle[:-2]
    cycle_length = len(cycle)
    return cycle[n-(n//cycle_length)*cycle_length]


if __name__ == '__main__':
    # import random
    # while True:
    #     n = random.randint(0, 10000)
    #     m = random.randint(2, 1000)
    #     print(n, m)
    #     if get_fibonacci_huge_algo(n,m) != get_fibonacci_huge_naive(n, m):
    #         print(get_fibonacci_huge_algo(n, m))
    #         print(get_fibonacci_huge_naive(n, m))
    #         break
    # n = 1000
    # m = 20
    # print(get_fibonacci_huge_algo(n, m))

    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_algo(n, m))
