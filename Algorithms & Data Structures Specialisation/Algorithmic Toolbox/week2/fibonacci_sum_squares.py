# Uses python3
from sys import stdin


def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


def find_cycle():
    cycle_start = [0, 1, 2, 6, 5, 0, 4, 3, 4, 0]
    cycle = []
    i = 0
    while len(cycle) <= len(cycle_start) or cycle[-len(cycle_start):] != cycle_start:
        cycle.append(fibonacci_sum_squares_naive(i))
        i = i+1

    return cycle[:-len(cycle_start)]


def fibonacci_sum_squares_algo(n):
    cycle = find_cycle()
    l = len(cycle)
    return cycle[n-(n//l)*l]


if __name__ == '__main__':
    # for i in range(1000):
    #     print(i)
    #     if fibonacci_sum_squares_naive(i) != fibonacci_sum_squares_algo(i):
    #         print(i)
    #         break
    n = int(stdin.read())
    print(fibonacci_sum_squares_algo(n))
