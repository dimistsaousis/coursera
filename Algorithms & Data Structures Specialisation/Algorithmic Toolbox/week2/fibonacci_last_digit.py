# Uses python3
import sys


def calc_fib(n):
    if n <= 1:
        return n
    c_prev = 0
    c_curr = 1
    for i in range(2, n+1):
        c_prev, c_curr = c_curr, (c_prev+c_curr) % 10
    return c_curr


def get_fibonacci_last_digit(n):
    if n <= 1:
        return 1

    c_prev = 0
    c_curr = 1
    last_digit_sum = 1
    for i in range(2, n+1):
        c_prev, c_curr = c_curr, (c_prev + c_curr) % 10
        last_digit_sum = last_digit_sum + c_curr
    return last_digit_sum

# def naive(n):
#     s = 1
#     c_prev = 0
#     c_curr= 1
#     for i in range(2, n+1):



if __name__ == '__main__':
    import random
    # while True:
    #     print(get_fibonacci_last_digit_naive(random.randint(0,1000)))
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
