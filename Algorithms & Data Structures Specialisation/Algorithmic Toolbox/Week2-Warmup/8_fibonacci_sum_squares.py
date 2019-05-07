"""
Task. Compute the last digit of 𝐹0^2 + 𝐹1^2 + 𝐹𝑛^2.
Input Format. Integer 𝑛.
Constraints. 0 ≤ 𝑛 ≤ 1018.
Output Format. The last digit of 𝐹0^2 + 𝐹1^2 + · · · + 𝐹n^2
"""


def get_fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    cum_sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        cum_sum += current * current

    return cum_sum % 10


def find_cycle():
    cycle_start = [0, 1, 2, 6, 5, 0, 4, 3, 4, 0]
    cycle = []
    i = 0
    while len(cycle) <= len(cycle_start) or cycle[-len(cycle_start):] != cycle_start:
        cycle.append(get_fibonacci_sum_squares_naive(i))
        i = i+1

    return cycle[:-len(cycle_start)]


def get_fibonacci_sum_squares_fast(n):
    cycle = find_cycle()
    l = len(cycle)
    return cycle[n-(n//l)*l]


def sanity_check():
    for i in range(1000):
        print(i)
        if get_fibonacci_sum_squares_naive(i) != get_fibonacci_sum_squares_fast(i):
            print(i)
            break


if __name__ == '__main__':
    n_ = int(input())
    print(get_fibonacci_sum_squares_fast(n_))
