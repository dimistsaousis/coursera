#Uses python3
import sys
import math
import queue


def segment_length(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)


def minimum_distance(x, y):
    vertex_size = len(x)
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
                    w = segment_length(x[v], y[v], x[u], y[u])
                    if w < cost[u]:
                        cost[u] = w
                        q.put((w, u))
            checked[v] = 1
    return sum(cost)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
