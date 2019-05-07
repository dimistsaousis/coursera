"""
Task. The goal of this problem is to represent a given positive integer 𝑛 as a sum of as many pairwise
distinct positive integers as possible. That is, to find the maximum 𝑘 such that 𝑛 can be written as
𝑎1 + 𝑎2 + · · · + 𝑎𝑘 where 𝑎1, . . . , 𝑎𝑘 are positive integers and 𝑎𝑖 != 𝑎𝑗 for all 1 ≤ 𝑖 < 𝑗 ≤ 𝑘.

Input Format. The input consists of a single integer 𝑛.
Constraints. 1 ≤ 𝑛 ≤ 109.

Output Format. In the first line, output the maximum number 𝑘 such that 𝑛 can be represented as a sum
of 𝑘 pairwise distinct positive integers. In the second line, output 𝑘 pairwise distinct positive integers
that sum up to 𝑛 (if there are many such representations, output any of them).
"""


def is_greater_or_equal(no1, no2):
    if no2 == -1:
        return True
    d1 = int(str(no1) + str(no2))
    d2 = int(str(no2) + str(no1))
    return d1 >= d2


def get_largest_number(a):
    res = ""
    while len(a) > 0:
        max_digit = -1
        max_digit_idx = -1

        for i, d in enumerate(a):
            if is_greater_or_equal(d, max_digit):
                max_digit = d
                max_digit_idx = i

        a.pop(max_digit_idx)
        res += str(max_digit)

    return res


def stringify(k):
    s = ""
    for el in k:
        s += str(el)
    return int(s)


def get_largest_number_naive(a):
    import itertools
    return str(max([stringify(k) for k in itertools.permutations(a)]))


if __name__ == '__main__':
    data = input().split()
    a_= data[1:]
    print(get_largest_number(a_))

