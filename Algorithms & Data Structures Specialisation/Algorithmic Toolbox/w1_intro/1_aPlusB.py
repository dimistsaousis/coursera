"""
We start from this ridiculously simple problem to show you the
pipeline of reading the problem statement, designing an algorithm, implementing it,
testing and debugging your program, and submitting it to
the grading system.
Input format. Integers a and b on the same line (separated by a space).
Output format. The sum of a and b.
"""


def sum_of_two_digits(first_digit, second_digit):
    return first_digit + second_digit


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(sum_of_two_digits(a, b))
