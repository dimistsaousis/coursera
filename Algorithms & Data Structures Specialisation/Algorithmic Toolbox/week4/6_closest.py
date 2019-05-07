#Uses python3
import sys
import math


def get_minimum_distance(ax, ay):
    n = len(ax)
    if n <= 3:
        return brute(ax)

    mid = n//2

    Lx = ax[:mid]
    Rx = ax[mid+1:]

    midpoint = ax[mid][0]
    Ly = []
    Ry = []
    for x in ay:
        if x[0] <= midpoint:
            Ly.append(x)
        else:
            Ry.append(x)

    d1 = get_minimum_distance(Lx, Ly)
    d2 = get_minimum_distance(Rx, Ry)

    d = min(d1, d2)

    valid = [x for x in ay if abs(x[0] - midpoint) < d]
    valid_n = len(valid)

    for i in range(valid_n-1):
        max_id = min(i+7, valid_n)
        for j in range(i+1, max_id):
            if valid[j][1] - valid[i][1] >= d:
                break
            d = min(d, dist(valid[i], valid[j]))
    return d


def prepare(x, y):
    a = list(zip(x, y))
    ax = sorted(a, key=lambda x: x[0])
    ay = sorted(a, key=lambda x: x[1])
    return get_minimum_distance(ax, ay)


def brute(ax):
    ln_ax = len(ax)
    if ln_ax == 1:
        return 10**10
    mi = dist(ax[0], ax[1])
    if ln_ax == 2:
        return mi
    for i in range(ln_ax):
        for j in range(i+1, ln_ax):
            if not(i == 0 and j == 1):
                d = dist(ax[i], ax[j])
                if d < mi:
                    mi = d
    return mi


def dist(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1]-p2[1])**2)**0.5


def naive(x, y):
    n = len(x)
    d = -1
    for i in range(n):
        for j in range(i+1, n):
            dmin = ((x[i]-x[j])**2 + (y[i]-y[j])**2)**0.5
            if d < 0 or d > dmin:
                d = dmin
    return d


if __name__ == '__main__':
    # import random
    # while True:
        # n = random.randint(2,5)
        # x = []
        # y = []
        # for _ in range(n):
        #     x.append(random.randint(-5, 5))
        #     y.append(random.randint(-5, 5))
        # x = [1, -4, 4]
        # y = [5, -4, -4]
        # if prepare(x, y) != naive(x, y):
        #     # print(prepare(x, y), naive(x, y))
        #     print(x)
        #     print(y)
        #     break
        # else:
        #     print('OK')

    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(prepare(x, y)))

