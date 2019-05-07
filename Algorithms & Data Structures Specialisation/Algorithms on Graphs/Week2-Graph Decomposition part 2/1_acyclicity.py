"""
Task. Check whether a given directed graph with 𝑛 vertices and 𝑚 edges contains a cycle.

Input Format. A graph is given in the standard format.

Constraints. 1 ≤ 𝑛 ≤ 103 , 0 ≤ 𝑚 ≤ 103 .

Output Format. Output 1 if the graph contains a cycle and 0 otherwise.
"""
import sys


def explore(adj_array, x, visited=None):
    visited = [] if visited is None else visited

    for w in adj_array[x]:
        if w not in visited:
            visited.append(w)
            visited = explore(adj_array, w, visited)
    return visited


def is_cycle(adj_array):
    n = len(adj_array)

    for i in range(n):
        stack = explore(adj_array, i)
        if i in stack:
            return 1
    return 0


if __name__ == '__main__':
    inp = sys.stdin.read()
    data = list(map(int, inp.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(is_cycle(adj))
