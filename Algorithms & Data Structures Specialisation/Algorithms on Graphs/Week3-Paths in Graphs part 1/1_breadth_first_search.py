"""
Task. Given an undirected graph with n vertices and m edges and two vertices u and v, compute the length
of a shortest path between u and v (that is, the minimum number of edges in a path from u to v).

Input Format. A graph is given in the standard format. The next line contains two vertices u and v.

Constraints. 2 ≤ n ≤ 105, 0 ≤ m ≤ 105, u 6= v, 1 ≤ u, v ≤ n.

Output Format. Output the minimum number of edges in a path from u to v, or −1 if there is no path.
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


def bfs(adj_array, s, t):
    adj_len = len(adj_array)
    dist = [-1 for _ in range(adj_len)]
    dist[s] = 0
    q = Queue()
    q.add(s)

    while not q.empty():
        u = q.next()
        for v in adj_array[u]:
            if v == t:
                return dist[u]+1
            if dist[v] == -1:
                q.add(v)
                dist[v] = dist[u]+1
    return -1


def distance(adj_array, s, t):
    return bfs(adj_array, s, t)


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
    s_, t_ = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s_, t_))
