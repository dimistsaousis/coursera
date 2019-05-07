"""
Task. You are given a set of points on a line and a set of segments on a line. The goal is to compute, for
each point, the number of segments that contain this point.

Input Format. The first line contains two non-negative integers 𝑠 and 𝑝 defining the number of segments
and the number of points on a line, respectively. The next 𝑠 lines contain two integers 𝑎𝑖, 𝑏𝑖 defining the 𝑖-th segment
[𝑎𝑖, 𝑏𝑖]. The next line contains 𝑝 integers defining points 𝑥1, 𝑥2, . . . , 𝑥𝑝.

Constraints. 1 ≤ 𝑠, 𝑝 ≤ 50000; −108 ≤ 𝑎𝑖 ≤ 𝑏𝑖 ≤ 108 for all 0 ≤ 𝑖 < 𝑠; −108 ≤ 𝑥𝑗 ≤ 108 for all 0 ≤ 𝑗 < 𝑝.

Output Format. Output 𝑝 non-negative integers 𝑘0, 𝑘1, . . . , 𝑘𝑝−1 where 𝑘𝑖 is the number of segments which contain 𝑥𝑖.
More formally, 𝑘𝑖 = |{𝑗 : 𝑎𝑗 ≤ 𝑥𝑖 ≤ 𝑏𝑗}|.
"""


def partition(array, low, high):
    el_low = array[low]
    idx_1 = low

    # Strictly smaller
    for i in range(low+1, high+1):
        if is_less(array[i], el_low):
            idx_1 += 1
            array[i], array[idx_1] = array[idx_1], array[i]
    array[low], array[idx_1] = array[idx_1], array[low]

    idx_2 = idx_1

    # Equal
    for i in range(idx_1+1, high+1):
        if is_equal(array[i], el_low):
            idx_2 += 1
            array[i], array[idx_2] = array[idx_2], array[i]

    return idx_1, idx_2


def randomized_quick_sort(array, left, right):
    import random

    if left >= right:
        return array
    k = random.randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


def is_less(element1, element2):
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


def is_equal(element1, element2):
    if element1[0] == element2[0] and element1[1][0] == element2[1][0]:
        return True
    return False


def create_plane(start, end, points):
    n_points = len(points)
    n_segments = len(start)
    lefts = [(start[k], 'l') for k in range(n_segments)]
    rights = [(end[k], 'r') for k in range(n_segments)]
    ps = [(points[k], "p" + str(k)) for k in range(n_points)]
    plane = lefts+rights+ps
    return plane


def count_segments_fast(start, end, points):
    n_points = len(points)
    n_segments = len(start)
    cnt = [0] * n_points

    lefts = [(start[k], 'l') for k in range(n_segments)]
    rights = [(end[k], 'r') for k in range(n_segments)]
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


def count_segments_naive(start, end, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(start)):
            if start[j] <= points[i] <= end[j]:
                cnt[i] += 1
    return cnt


def sanity_check():
    import random
    while True:
        number_of_points = random.randint(1, 50)
        number_of_segments = random.randint(1, 100)
        points = []
        start = []
        end = []
        for _ in range(number_of_points):
            points.append(random.randint(0, 100))
        for _ in range(number_of_segments):
            start.append(random.randint(0, 50))
            end.append(random.randint(start[-1], 100))

        if count_segments_naive(start, end, points) != count_segments_fast(start, end, points):
            print(create_plane(start, end, points))
            break
        else:
            print("OK")


if __name__ == '__main__':
    data = list(map(int, input().split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    pts = data[2 * n + 2:]
    res = count_segments_fast(starts, ends, pts)
    for x in res:
        print(x, end=' ')

