"""
Task. Given an undirected graph and two distinct vertices 𝑢 and 𝑣, check if there is a path between 𝑢 and 𝑣.

Input Format. An undirected graph with 𝑛 vertices and 𝑚 edges. The next line contains two vertices 𝑢
and 𝑣 of the graph.

Constraints. 2 ≤ 𝑛 ≤ 103 ; 1 ≤ 𝑚 ≤ 103 ; 1 ≤ 𝑢, 𝑣 ≤ 𝑛; 𝑢 ̸= 𝑣.

Output Format. Output 1 if there is a path between 𝑢 and 𝑣 and 0 otherwise.
"""
import sys


def explore(adj_array, x, visited=None):
    visited = [] if visited is None else visited
    visited.append(x)

    for w in adj_array[x]:
        if w not in visited:
            visited = explore(adj_array, w, visited)
    return visited


def number_of_components(adj_array):
    visited = []
    components = 0
    for i in range(len(adj_array)):
        if i not in visited:
            components += 1
            visited += explore(adj_array, i)

    return components


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
    print(number_of_components(adj))
