"""
Task. Given two integers 𝑎 and 𝑏, find their greatest common divisor.
Input Format. The two integers 𝑎, 𝑏 are given in the same line separated by space.
Constraints. 1 ≤ 𝑎, 𝑏 ≤ 2 · 109.
Output Format. Output GCD(𝑎, 𝑏).
"""


def get_gcd_naive(a, b):
    gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            gcd = d
    return gcd


def get_gcd_fast(a, b):
    if a > b:
        a, b = b, a

    if a == 0:
        return b
    else:
        b = b - b//a*a
        return get_gcd_fast(b, a)


def sanity_check():
    import random
    while True:
        a, b = random.randint(1, 100), random.randint(1, 100)
        res_fast, res_naive = get_gcd_fast(a, b), get_gcd_naive(a, b)

        if res_fast != res_naive:
            print(a, b, res_fast, res_naive)
            break
        else:
            print('OK')


if __name__ == "__main__":
    input_ab = input()
    a_, b_ = map(int, input_ab.split())
    print(get_gcd_fast(a_, b_))
