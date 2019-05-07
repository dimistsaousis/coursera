# Uses python3
import sys


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def fibonacci_partial_sum_algo(start, end):
    cycle = []
    for i in range(60):
        cycle.append(fibonacci_sum_naive(i))

    cycle_length = len(cycle)

    my_start = start - (start//cycle_length)*cycle_length
    my_end = end - (end//cycle_length)*cycle_length
    return (cycle[my_end] - cycle[my_start-1]) % 10


def fibonacci_partial_sum_naive(from_, to):
    sum = 0
    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


if __name__ == '__main__':
    # import random
    # while True:
    #     s = random.randint(0, 50000)
    #     e = random.randint(s, 50000)
    #     print(s, e)
    #     if fibonacci_partial_sum_algo(s,e) != fibonacci_partial_sum_naive(s, e):
    #         print(fibonacci_partial_sum_algo(s,e))
    #         print(fibonacci_partial_sum_naive(s, e))
    #         break

    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_algo(from_, to))
