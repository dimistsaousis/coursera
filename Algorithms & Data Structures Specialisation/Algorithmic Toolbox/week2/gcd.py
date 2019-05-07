# Uses python3
import sys


def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_algo(a, b):
    if a > b:
        a, b = b, a

    if a == 0:
        return b
    else:
        b = b - int(b/a)*a
        return gcd_algo(b, a)


if __name__ == "__main__":
    # import random
    # while True:
    #     a = random.randint(1,100)
    #     b = random.randint(1,100)
    #     print(a, b)
    #     if gcd_naive(a,b) != gcd_algo(a,b):
    #         print(gcd_naive(a, b))
    #         print(gcd_algo(a,b))
    #         break

    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_algo(a, b))
