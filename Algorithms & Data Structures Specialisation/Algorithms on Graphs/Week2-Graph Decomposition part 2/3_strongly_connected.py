"""
Task. Compute the number of strongly connected components of a given directed graph with 𝑛 vertices and
𝑚 edges.

Input Format. A graph is given in the standard format.

Constraints. 1 ≤ 𝑛 ≤ 104, 0 ≤ 𝑚 ≤ 104.

Output Format. Output the number of strongly connected components.
"""

import sys

sys.setrecursionlimit(200000)


def dfs_with_order(adj_array, used, order, x, clock):
    used[x] = 1
    clock += 1
    for w in adj_array[x]:
        if used[w] == 0:
            used, order, clock = dfs_with_order(adj_array, used, order, w, clock)
    order[x] = clock
    clock += 1
    return used, order, clock


def dfs(adj, used, x):
    used[x] = 1
    for w in adj[x]:
        if used[w] == 0:
            used = dfs(adj, used, w)
    return used


def topological_sort(adj_array):
    n = len(adj_array)
    used = [0] * n
    order = [0] * n
    clock = 1
    for i in range(n):
        if used[i] == 0:
            used, order, clock = dfs_with_order(adj_array, used, order, i, clock)
    idx = [i for i in range(n)]
    return sorted(idx, key=lambda k: order[k], reverse=True)


def number_of_strongly_connected_components(adj_array, adj_reverse):
    n = len(adj_array)
    used = [0] * n
    result = 0
    idx = topological_sort(adj_reverse)
    for i in idx:
        if used[i] == 0:
            result += 1
            used = dfs(adj_array, used, i)
    return result


if __name__ == '__main__':
    inp = sys.stdin.read()
    data = list(map(int, inp.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    adj_reverse_ = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj_reverse_[b-1].append(a-1)
    print(number_of_strongly_connected_components(adj, adj_reverse_))
