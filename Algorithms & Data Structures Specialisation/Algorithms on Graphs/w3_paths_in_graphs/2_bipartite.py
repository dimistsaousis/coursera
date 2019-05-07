"""
Task. Given an undirected graph with n vertices and m edges, check whether it is bipartite.

Input Format. A graph is given in the standard format.

Constraints. 1 ≤ n ≤ 105, 0 ≤ m ≤ 105.

Output Format. Output 1 if the graph is bipartite and 0 otherwise.
"""

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


def bipartite(adj_arr):
    s = 0
    adj_len = len(adj_arr)
    colors = [-1 for _ in range(adj_len)]
    colors[s] = 0
    q = Queue()
    q.add(s)

    while not q.empty():
        u = q.next()
        for v in adj_arr[u]:
            if colors[v] == -1:
                q.add(v)
                colors[v] = (colors[u] + 1) % 2
            elif colors[u] == colors[v]:
                return 0
    return 1


if __name__ == '__main__':
    inp = sys.stdin.read()
    data = list(map(int, inp.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
