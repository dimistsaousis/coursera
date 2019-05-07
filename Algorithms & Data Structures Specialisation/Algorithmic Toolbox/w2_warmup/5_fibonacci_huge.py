"""
Task. Given two integers 𝑛 and 𝑚, output 𝐹𝑛 mod 𝑚 (that is, the remainder of 𝐹𝑛 when divided by 𝑚).
Input Format. The input consists of two integers 𝑛 and 𝑚 given on the same line (separated by a space).
Constraints. 1 ≤ 𝑛 ≤ 1018, 2 ≤ 𝑚 ≤ 103.
Output Format. Output 𝐹𝑛 mod �
"""


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def calc_fib(n):
    fib_numbers = [0, 1]
    if n <= 1:
        return n

    for i in range(2, n+1):
        fib_numbers.append(fib_numbers[i-1] + fib_numbers[i-2])

    return fib_numbers[-1]


def get_fibonacci_huge_fast(n, m):
    if m == 1:
        return calc_fib(n)

    if n <= 1:
        return n

    cycle = [0, 1, 1]

    while (cycle[-2], cycle[-1]) != (0, 1):
        cycle.append((cycle[-2]+cycle[-1]) % m)

    cycle = cycle[:-2]
    cycle_length = len(cycle)
    return cycle[n-(n//cycle_length)*cycle_length]


def sanity_check():
    import random
    while True:
        n, m = random.randint(0, 10000), random.randint(2, 1000)

        res_naive, res_fast = get_fibonacci_huge_naive(n, m), get_fibonacci_huge_fast(n,m)

        if res_naive != res_fast:
            print(res_naive, res_fast, n, m)
            break


if __name__ == '__main__':
    input_nm = input()
    n_, m_ = map(int, input_nm.split())
    print(get_fibonacci_huge_fast(n_, m_))
