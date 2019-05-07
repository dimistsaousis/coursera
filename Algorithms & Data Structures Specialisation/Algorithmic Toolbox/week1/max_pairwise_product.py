# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])
    return max_product


def fast_max_pairwise_product(numbers):
    max_1 = -1
    max_2 = -1
    for number in numbers:
        if max_2 < number:
            if max_1 < number:
                temp = max_1
                max_1 = number
                max_2 = temp
            else:
                max_2 = number
    return max_1 * max_2


if __name__ == '__main__':
    # import random
    # while True:
    #     k = random.randrange(2, 10)
    #     l = []
    #     for i in range(k):
    #         l.append(random.randrange(1, 500000))
    #     print(l)
    #     if fast_max_pairwise_product(l) == max_pairwise_product(l):
    #         print("OK")
    #     else:
    #         print("FALSE")
    #         break;

    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(fast_max_pairwise_product(input_numbers))
