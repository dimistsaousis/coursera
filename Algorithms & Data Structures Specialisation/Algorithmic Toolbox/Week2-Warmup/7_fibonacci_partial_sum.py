"""
Task. Given two non-negative integers 𝑚 and 𝑛, where 𝑚 ≤ 𝑛, find the last digit of the sum 𝐹𝑚 + 𝐹𝑚+1 +· · · + 𝐹𝑛.
Input Format. The input consists of two non-negative integers 𝑚 and 𝑛 separated by a space.
Constraints. 0 ≤ 𝑚 ≤ 𝑛 ≤ 1018.
Output Format. Output the last digit of 𝐹𝑚 + 𝐹𝑚+1 + · · · + 𝐹𝑛.
"""


def get_fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    cum_sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        cum_sum += current

    return cum_sum % 10


def get_fibonacci_partial_sum_fast(start, end):
    cycle = []
    for i in range(60):
        cycle.append(get_fibonacci_sum_naive(i))

    cycle_length = len(cycle)

    my_start = start - (start//cycle_length)*cycle_length
    my_end = end - (end//cycle_length)*cycle_length
    return (cycle[my_end] - cycle[my_start-1]) % 10


def get_fibonacci_partial_sum_naive(start, end):
    cum_sum = 0
    previous = 0
    current = 1

    for i in range(end + 1):
        if i >= start:
            cum_sum += previous

        previous, current = current, previous + current

    return cum_sum % 10


def sanity_check():
    import random
    while True:
        start = random.randint(0, 50000)
        end = random.randint(s, 50000)
        res_fast, res_naive = get_fibonacci_partial_sum_fast(start, end), get_fibonacci_partial_sum_naive(start, end)
        if res_fast != res_naive:
            print(start, end, res_fast, res_naive)
            break


if __name__ == '__main__':
    se_input = input()
    s, e = map(int, se_input.split())
    print(get_fibonacci_partial_sum_fast(s, e))
