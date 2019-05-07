# Uses python3
import sys


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l
    return a*b


def gcd_algo(a, b):
    if a > b:
        a, b = b, a

    if a == 0:
        return b
    else:
        b = b - int(b/a)*a
        return gcd_algo(b, a)


def lcm_algo(a, b):
    if a == 0 and b == 0:
        return 0
    gcd = gcd_algo(a, b)
    lcm = a//gcd
    return lcm*b


if __name__ == '__main__':
    # print(lcm_algo(33, 45))
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_algo(a, b))

