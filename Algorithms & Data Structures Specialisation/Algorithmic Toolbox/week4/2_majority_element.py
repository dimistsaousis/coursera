# Uses python3
import sys


def is_majority(a, element):
    n = len(a)
    count = 0
    for i in range(n):
        if a[i] == element:
            count += 1
    if count > n/2:
        return element, True
    return None, False


def get_majority_element(a):
    n = len(a)

    if n == 2:
        if a[0] == a[1]:
            return a[0], True
        else:
            return None, False

    if n == 1:
        return a[0], True

    element1, flag1 = get_majority_element(a[:n//2])
    element2, flag2 = get_majority_element(a[n//2:])

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


def has_majority(a):
    x, flag = get_majority_element(a)
    if flag:
        return 1
    return 0


def naive(a):
    dic = {}
    for x in a:
        dic[x] = dic[x] + 1 if x in dic else 1
    if max(dic.values()) > len(a)/2:
        return 1
    return 0


if __name__ == '__main__':
    # import random
    #
    # while True:
    #     size = random.randint(2,20)
    #     l = []
    #     for _ in range(size):
    #         l.append(random.randint(0, 20))
    #
    #     if naive(l) != has_majority(l):
    #         print(l)
    #         break
    #     else:
    #         print("OK")

    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(has_majority(a))
