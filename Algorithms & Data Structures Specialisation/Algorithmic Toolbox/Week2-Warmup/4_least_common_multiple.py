"""
Task. Given two integers 𝑎 and 𝑏, find their least common multiple.
Input Format. The two integers 𝑎 and 𝑏 are given in the same line separated by space.
Constraints. 1 ≤ 𝑎, 𝑏 ≤ 2 · 109.
Output Format. Output the least common multiple of 𝑎 and 𝑏.
"""


def get_lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l
    return a*b


def get_gcd(a, b):
    if a > b:
        a, b = b, a

    if a == 0:
        return b
    else:
        b = b - int(b/a)*a
        return get_gcd(b, a)


def get_lcm_fast(a, b):
    if a == 0 and b == 0:
        return 0
    gcd = get_gcd(a, b)
    lcm = a//gcd
    return lcm*b


if __name__ == '__main__':
    ab_input = input()
    a_, b_ = map(int, ab_input.split())
    print(get_lcm_fast(a_, b_))
