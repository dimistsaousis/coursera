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


def bfs(adj, s, t):
    n = len(adj)
    dist = [-1 for _ in range(n)]
    dist[s] = 0
    q = Queue()
    q.add(s)

    while not q.empty():
        u = q.next()
        for v in adj[u]:
            if v == t:
                return dist[u]+1
            if dist[v] == -1:
                q.add(v)
                dist[v] = dist[u]+1
    return -1


def distance(adj, s, t):
    return bfs(adj, s, t)


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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
