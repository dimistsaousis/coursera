#Uses python3

import sys
import queue


class Queue:
    def __init__(self):
        self._array = []

    def next(self):
        return self._array.pop(0)

    def add(self, v):
        self._array.append(v)

    def empty(self):
        return len(self._array) == 0


def bipartite(adj):
    s = 0
    n = len(adj)
    colors = [-1 for _ in range(n)]
    colors[s] = 0
    q = Queue()
    q.add(s)

    while not q.empty():
        u = q.next()
        for v in adj[u]:
            if colors[v] == -1:
                q.add(v)
                colors[v] = (colors[u] + 1) % 2
            elif colors[u] == colors[v]:
                return 0
    return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
