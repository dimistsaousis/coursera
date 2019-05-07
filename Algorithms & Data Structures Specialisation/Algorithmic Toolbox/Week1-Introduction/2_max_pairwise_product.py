"""
Given a sequence of non-negative integers a1,...,an, compute max 1≤i,j≤n ai· aj
Note that i and j should be different, though it may be the case that ai = aj.
Input format.
The first line contains an integer n. The next line contains n non-negative integers a1,...,an (separated by spaces).
Output format. The maximum pairwise product.
Constraints. 2 ≤ n ≤ 2 · 105 ; 0 ≤ a1,...,an ≤ 2 · 105
"""


def naive_max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product, numbers[first] * numbers[second])
    return max_product


def fast_max_pairwise_product(numbers):
    max_1, max_2 = -1, -1

    for number in numbers:
        if max_2 < number:
            if max_1 < number:
                max_1, max_2 = number, max_1
            else:
                max_2 = number
    return max_1 * max_2


def sanity_check():
    import random
    while True:
        number_size = random.randrange(2, 10)
        numbers = list()

        for _ in range(number_size):
            number = random.randrange(1, 500000)
            numbers.append(number)

        if fast_max_pairwise_product(numbers) == naive_max_pairwise_product(numbers):
            print("OK")
        else:
            print(numbers)
            break


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(fast_max_pairwise_product(input_numbers))
