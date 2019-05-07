#Uses python3
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
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
