"""
Task. Compute a topological ordering of a given directed acyclic graph (DAG) with 𝑛 vertices and 𝑚 edges.

Input Format. A graph is given in the standard format.

Constraints. 1 ≤ 𝑛 ≤ 105, 0 ≤ 𝑚 ≤ 105. The given graph is guaranteed to be acyclic.

Output Format. Output any topological ordering of its vertices. (Many DAGs have more than just one
topological ordering. You may output any of them.)
"""

import sys


def dfs(adj_array, used, order, x, clock):
    used[x] = 1
    clock += 1
    for w in adj_array[x]:
        if used[w] == 0:
            used, order, clock = dfs(adj_array, used, order, w, clock)
    order[x] = clock
    clock += 1
    return used, order, clock


def topological_sort(adj_array):
    arr_len = len(adj_array)
    used = [0] * arr_len
    order = [0] * arr_len
    clock = 1
    for i in range(arr_len):
        if used[i] == 0:
            used, order, clock = dfs(adj_array, used, order, i, clock)
    idx = [i for i in range(arr_len)]
    return sorted(idx, key=lambda k: order[k], reverse=True)


if __name__ == '__main__':
    inp = sys.stdin.read()
    data = list(map(int, inp.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order_ = topological_sort(adj)
    for x in order_:
        print(x + 1, end=' ')

