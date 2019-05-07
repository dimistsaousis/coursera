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


def fibonacci_sum_algo(n):
    cycle = []
    for i in range(60):
        cycle.append(fibonacci_sum_naive(i))

    cycle_length = len(cycle)
    return cycle[n-(n//cycle_length)*cycle_length]



if __name__ == '__main__':

    # for _ in range(100000):
    #     print(_)
    #     if fibonacci_sum_algo(_) != fibonacci_sum_naive(_):
    #         print(_)
    #         break


    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_algo(n))
