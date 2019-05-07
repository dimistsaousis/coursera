"""
Task. Given an integer 𝑛, find the 𝑛th Fibonacci number 𝐹𝑛.
Input Format. The input consists of a single integer 𝑛.
Constraints. 0 ≤ 𝑛 ≤ 45.
Output Format. Output 𝐹𝑛.
"""


def calc_fib(n):
    fib_numbers = [0, 1]
    if n <= 1:
        return n

    for i in range(2, n+1):
        fib_numbers.append(fib_numbers[i-1] + fib_numbers[i-2])

    return fib_numbers[-1]
