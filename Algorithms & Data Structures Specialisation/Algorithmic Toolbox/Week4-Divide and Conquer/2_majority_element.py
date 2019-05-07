"""
Task. The goal in this code problem is to check whether an input sequence contains a majority element.

Input Format. The first line contains an integer 𝑛, the next one contains a sequence of 𝑛 non-negative
integers 𝑎0, 𝑎1, . . . , 𝑎𝑛−1.

Constraints. 1 ≤ 𝑛 ≤ 105 ; 0 ≤ 𝑎𝑖 ≤ 109 for all 0 ≤ 𝑖 < 𝑛.

Output Format. Output 1 if the sequence contains an element that appears strictly more than 𝑛/2 times,
and 0 otherwise.
"""


def is_majority(array, element):
    size_arr = len(array)
    count = 0

    for i in range(size_arr):
        if array[i] == element:
            count += 1

    if count > size_arr/2:
        return element, True

    return None, False


def get_majority_element(array):
    size_arr = len(array)

    if size_arr == 2:
        if array[0] == array[1]:
            return array[0], True
        else:
            return None, False

    if size_arr == 1:
        return a[0], True

    element1, flag1 = get_majority_element(array[:size_arr//2])
    element2, flag2 = get_majority_element(array[size_arr//2:])

    if flag1 and flag2:
        if element1 == element2:
            return element1, True

        element1, flag1 = is_majority(a, element1)
        element2, flag2 = is_majority(a, element2)

        if flag1:
            return element1, True

        if flag2:
            return element2, True

        return None, False

    if flag1:
        return is_majority(a, element1)

    if flag2:
        return is_majority(a, element2)

    return None, False


def has_majority_element(array):
    x, flag = get_majority_element(array)
    if flag:
        return 1
    return 0


def has_majority_element_naive(array):
    from collections import defaultdict

    counter = defaultdict(lambda: 1)
    for el in array:
        counter[el] += 1

    return 1 if max(counter.values()) > len(array)/2 else 0


def sanity_check():
    import random
    while True:
        size = random.randint(2, 20)
        array = []
        for _ in range(size):
            array.append(random.randint(0, 20))

        if has_majority_element_naive(array) != has_majority_element(array):
            print(array)
            break
        else:
            print("OK")


if __name__ == '__main__':
    n, *a = list(map(int, input().split()))
    print(has_majority_element(a))
