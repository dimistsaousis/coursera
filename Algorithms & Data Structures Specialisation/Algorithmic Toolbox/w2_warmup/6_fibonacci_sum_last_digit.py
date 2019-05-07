"""
Task. Given an integer 𝑛, find the last digit of the sum 𝐹0 + 𝐹1 + · · · + 𝐹𝑛.
Input Format. The input consists of a single integer 𝑛.
Constraints. 0 ≤ 𝑛 ≤ 1018.
Output Format. Output the last digit of 𝐹0 + 𝐹1 + · · · + 𝐹𝑛.
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


def get_fibonacci_sum_fast(n):
    cycle = []
    for i in range(60):
        cycle.append(get_fibonacci_sum_naive(i))

    cycle_length = len(cycle)
    return cycle[n-(n//cycle_length)*cycle_length]


def sanity_check():
    for i in range(100000):
        if get_fibonacci_sum_fast(i) != get_fibonacci_sum_naive(i):
            print(i)
            break


if __name__ == '__main__':
    n_input = int(input())
    print(get_fibonacci_sum_fast(n_input))
