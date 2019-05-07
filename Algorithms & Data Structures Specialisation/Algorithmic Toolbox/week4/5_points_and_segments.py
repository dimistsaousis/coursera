# Uses python3
import sys
import random


def partition(a, low, high):
    x = a[low]
    m1 = low

    # Strictly smaller
    for i in range(low+1, high+1):
        if less(a[i], x):
            m1 += 1
            a[i], a[m1] = a[m1], a[i]
    a[low], a[m1] = a[m1], a[low]

    m2 = m1

    # Equal
    for i in range(m1+1, high+1):
        if equal(a[i], x):
            m2 += 1
            a[i], a[m2] = a[m2], a[i]

    return m1, m2


def randomized_quick_sort(a, l, r):
    if l >= r:
        return a
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition(a, l, r)
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)


def less(element1, element2):
    if element1[0] < element2[0]:
        return True
    elif element1[0] > element2[0]:
        return False
    else:
        type1 = element1[1][0]
        type2 = element2[1][0]

        if type1 == type2:
            return False
        if type1 == 'l':
            return True
        if type1 == 'p' and type2 != 'p' and type2 != 'l':
            return True
        return False


def equal(element1, element2):
    if element1[0] == element2[0] and element1[1][0] == element2[1][0]:
        return True
    return False


def create_plane(starts, ends, points):
    n_points = len(points)
    n_segments = len(starts)
    lefts = [(starts[k], 'l') for k in range(n_segments)]
    rights = [(ends[k], 'r') for k in range(n_segments)]
    ps = [(points[k], "p" + str(k)) for k in range(n_points)]
    plane = lefts+rights+ps
    return plane


def fast_count_segments(starts, ends, points):
    n_points = len(points)
    n_segments = len(starts)
    cnt = [0] * n_points

    lefts = [(starts[k], 'l') for k in range(n_segments)]
    rights = [(ends[k], 'r') for k in range(n_segments)]
    ps = [(points[k], "p"+str(k)) for k in range(n_points)]
    plane = lefts+rights+ps
    randomized_quick_sort(plane, 0, len(plane)-1)

    count_lefts = 0
    count_rights = 0
    for k in plane:
        if k[1] == 'l':
            count_lefts += 1
        elif k[1] == 'r':
            count_rights += 1
        else:
            idx = int(k[1][1:])
            cnt[idx] = count_lefts - count_rights
    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == '__main__':
    # while True:
    #     number_of_points = random.randint(1, 50)
    #     number_of_segments = random.randint(1, 100)
    #     points = []
    #     starts = []
    #     ends = []
    #     for _ in range(number_of_points):
    #         points.append(random.randint(0, 100))
    #     for _ in range(number_of_segments):
    #         starts.append(random.randint(0, 50))
    #         ends.append(random.randint(starts[-1], 100))
    #
    #     if naive_count_segments(starts, ends, points) != fast_count_segments(starts, ends, points):
    #         print(create_plane(starts, ends, points))
    #         break
    #     else:
    #         print("OK")

    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')

