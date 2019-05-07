"""
Task. Given n points on a plane and an integer k, compute the largest possible value of d such that the
given points can be partitioned into k non-empty subsets in such a way that the distance between any
two points from different subsets is at least d.

Input Format. The first line contains the number n of points. Each of the following n lines defines a point
(xi , yi). The last line contains the number k of clusters.

Constraints. 2 ≤ k ≤ n ≤ 200; −103 ≤ xi , yi ≤ 103 are integers. All points are pairwise different.

Output Format. Output the largest value of d. The absolute value of the difference between the answer of
your program and the optimal value should be at most 10−6. To ensure this, output your answer with at least seven
digits after the decimal point (otherwise your answer, while being computed correctly, can turn out to be wrong
because of rounding issues).
"""
import sys
import math
import queue


def dist(node_1, node_2):
    return math.sqrt((node_1.x-node_2.x)**2+(node_1.y-node_2.y)**2)


class Node:
    def __init__(self, id, x, y):
        self.parent = self
        self.x = x
        self.y = y
        self.id = id

    def __repr__(self):
        return "(x="+str(self.x) + ",y=" + str(self.y) + ")"


def make_set(id, x, y):
    return Node(id, x, y)


def find(node):
    if node.parent != node:
        node.parent = find(node.parent)
    return node.parent


def union(node_x, node_y):
    x_root = find(node_x)
    y_root = find(node_y)
    if x_root == y_root:
        return
    y_root.parent = x_root


def kruskal(x, y, k):
    total_vertices = len(x)
    vertex = []
    for i in range(total_vertices):
        vertex.append(make_set(i, x[i], y[i]))
    edges = []

    for i in range(total_vertices):
        for j in range(i+1, total_vertices):
            edges.append((vertex[i], vertex[j], dist(vertex[i], vertex[j])))

    edges = sorted(edges, key=lambda x: x[2])
    end_set = []
    for u, v, d in edges:
        if find(u) != find(v):
            end_set.append(d)
            union(u, v)

    return end_set[-(k-1)]


def clustering(x, y, k):
    return kruskal(x, y, k)


if __name__ == '__main__':
    inp = sys.stdin.read()
    data = list(map(int, inp.split()))
    n = data[0]
    data = data[1:]
    x_ = data[0:2 * n:2]
    y_ = data[1:2 * n:2]
    data = data[2 * n:]
    k_ = data[0]
    print("{0:.9f}".format(clustering(x_, y_, k_)))
