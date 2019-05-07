#Uses python3

import sys


def greater_or_equal(no1, no2):
    if no2 == -1:
        return True
    d1 = int(str(no1) + str(no2))
    d2 = int(str(no2) + str(no1))
    return d1 >= d2


def largest_number(a):
    res = ""
    while len(a) > 0:
        max_digit = -1
        max_digit_idx = -1

        for i, d in enumerate(a):
            if greater_or_equal(d, max_digit):
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


def naive(a):
    import itertools
    return str(max([stringify(k) for k in itertools.permutations(a)]))


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

