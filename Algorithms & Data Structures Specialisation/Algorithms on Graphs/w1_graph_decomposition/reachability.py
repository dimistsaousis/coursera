"""
Task. Given an undirected graph with 𝑛 vertices and 𝑚 edges, compute the number of connected components in it.

Input Format. A graph is given in the standard format.

Constraints. 1 ≤ 𝑛 ≤ 103, 0 ≤ 𝑚 ≤ 103.

Output Format. Output the number of connected components.
"""

import sys


def explore(adj_array, x, y, visited=None):
    visited = [] if visited is None else visited
    visited.append(x)

    for w in adj_array[x]:
        if w == y:
            return True
        if w not in visited:
            if explore(adj_array, w, y, visited):
                return True

    return False


def reach(adj_array, x, y):
    return 1 if explore(adj_array, x, y) else 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
