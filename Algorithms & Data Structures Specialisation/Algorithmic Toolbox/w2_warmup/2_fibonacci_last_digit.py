"""
Task. Given an integer 𝑛, find the last digit of the 𝑛th Fibonacci number 𝐹𝑛 (that is, 𝐹𝑛 mod 10).
Input Format. The input consists of a single integer 𝑛.
Constraints. 0 ≤ 𝑛 ≤ 107.
Output Format. Output the last digit of 𝐹𝑛.
"""


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


if __name__ == '__main__':
    n_input = int(input())
    print(get_fibonacci_last_digit(n_input))
