"""
Task. Given n points on a plane, connect them with segments of minimum total length such that there is a
path between any two points. Recall that the length of a segment with endpoints (x1, y1) and (x2, y2) is equal to p
(x1 − x2) 2 + (y1 − y2) 2.

Input Format. The first line contains the number n of points. Each of the following n lines defines a point
(xi, yi).

Constraints. 1 ≤ n ≤ 200; −103 ≤ xi , yi ≤ 103 are integers. All points are pairwise different, no three
points lie on the same line.

Output Format. Output the minimum total length of segments. The absolute value of the difference
between the answer of your program and the optimal value should be at most 10−6
. To ensure this, output your answer with at least seven digits after the decimal point (otherwise your answer, while
being computed correctly, can turn out to be wrong because of rounding issues).
"""

import sys
import math
import queue


def segment_length(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)


def minimum_distance(pts_x, pts_y):
    vertex_size = len(pts_x)
    cost = [float('inf')]*vertex_size
    checked = [0]*vertex_size
    cost[0] = 0
    q = queue.PriorityQueue()
    for i in range(vertex_size):
        q.put((cost[i], i))

    while not q.empty():
        _, v = q.get()
        while not q.empty() and checked[v] == 1:
            _, v = q.get()
        if checked[v] != 1:
            for u in range(vertex_size):
                if checked[u] == 0 and u != v:
                    w = segment_length(pts_x[v], pts_y[v], pts_x[u], pts_y[u])
                    if w < cost[u]:
                        cost[u] = w
                        q.put((w, u))
            checked[v] = 1
    return sum(cost)


if __name__ == '__main__':
    inp = sys.stdin.read()
    data = list(map(int, inp.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
