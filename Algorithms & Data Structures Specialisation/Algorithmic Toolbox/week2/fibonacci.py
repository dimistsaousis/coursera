# Uses python3
import sys


def calc_fib(n):
    l = [0, 1]
    if n <= 1:
        return n
    for i in range(2, n+1):
        l.append(l[i-1] + l[i-2])
    return l[-1]


n = int(input())
print(calc_fib(n))
