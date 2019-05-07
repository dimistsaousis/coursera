"""
Task. Given 𝑛 points on a plane, find the smallest distance between a pair of two (different) points. Recall
that the distance between points (𝑥1, 𝑦1) and (𝑥2, 𝑦2) is equal to √(𝑥1 − 𝑥2)^2 + (𝑦1 − 𝑦2)^2.

Input Format. The first line contains the number 𝑛 of points. Each of the following 𝑛 lines defines a point (𝑥𝑖, 𝑦𝑖).

Constraints. 2 ≤ 𝑛 ≤ 105 ; −109 ≤ 𝑥𝑖 , 𝑦𝑖 ≤ 109 are integers.

Output Format. Output the minimum distance. The absolute value of the difference between the answer of your program
and the optimal value should be at most 10−3. To ensure this, output your answer with at least four digits after the
decimal point (otherwise your answer, while being computed correctly, can turn out to be wrong because of rounding
issues).
"""


def pre_process(pts_x, pts_y):
    pts = list(zip(pts_x, pts_y))
    pts_x_sorted = sorted(pts, key=lambda z: z[0])
    pts_y_sorted = sorted(pts, key=lambda z: z[1])
    return pts_x_sorted, pts_y_sorted


def get_minimum_distance(pts_x, pts_y):
    pts_x, pts_y = pre_process(pts_x, pts_y)
    pts_len = len(pts_x)

    if pts_len <= 3:
        return get_minimum_distance_brute(pts_x)

    mid = pts_len//2

    left_x = pts_x[:mid]
    right_x = pts_x[mid + 1:]

    mid_x = pts_x[mid][0]
    left_y = []
    right_y = []

    for pt_y in pts_y:
        if pt_y[0] <= mid_x:
            left_y.append(pt_y)
        else:
            right_y.append(pt_y)

    dist_1 = get_minimum_distance(left_x, left_y)
    dist_2 = get_minimum_distance(right_x, right_y)

    dist_min = min(dist_1, dist_2)

    valid = [pt_y for pt_y in pts_y if abs(pt_y[0] - mid_x) < dist_min]
    valid_size = len(valid)

    for i in range(valid_size-1):
        max_id = min(i+7, valid_size)
        for j in range(i+1, max_id):
            if valid[j][1] - valid[i][1] >= dist_min:
                break
            dist_min = min(dist_min, dist_min(valid[i], valid[j]))
    return dist_min


def get_minimum_distance_brute(pts):
    pts_len = len(pts)
    if pts_len == 1:
        return 10**10

    dist_min = get_distance(pts[0], pts[1])

    if pts_len == 2:
        return dist_min

    for i in range(pts_len):
        for j in range(i+1, pts_len):
            if not(i == 0 and j == 1):
                d = get_distance(pts[i], pts[j])
                if d < dist_min:
                    dist_min = d

    return dist_min


def get_distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1]-p2[1])**2)**0.5


def get_minimum_distance_naive(pts_x, pts_y):
    pts_len = len(pts_x)
    res = -1
    for i in range(pts_len):
        for j in range(i+1, pts_len):
            dist_min = ((pts_x[i] - pts_x[j]) ** 2 + (pts_y[i] - pts_y[j]) ** 2) ** 0.5
            if res < 0 or res > dist_min:
                res = dist_min
    return res


def sanity_check():
    import random
    while True:
        pts_len = random.randint(2, 5)
        pts_x = []
        pts_y = []

        for _ in range(pts_len):
            pts_x.append(random.randint(-5, 5))
            pts_y.append(random.randint(-5, 5))

        if get_minimum_distance(pts_x, pts_y) != get_minimum_distance_naive(pts_x, pts_y):
            print(pts_x)
            print(pts_y)
            break
        else:
            print('OK')


if __name__ == '__main__':
    data = list(map(int, input().split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(pre_process(x, y)))

