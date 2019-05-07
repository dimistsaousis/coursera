#Uses python3

import sys


def dfs(adj, used, order, x, clock):
    used[x] = 1
    clock += 1
    for w in adj[x]:
        if used[w] == 0:
            used, order, clock = dfs(adj, used, order, w, clock)
    order[x] = clock
    clock += 1
    return used, order, clock


def toposort(adj):
    n = len(adj)
    used = [0] * n
    order = [0] * n
    clock = 1
    for i in range(n):
        if used[i] == 0:
            used, order, clock = dfs(adj, used, order, i, clock)
    idx = [i for i in range(n)]
    return sorted(idx, key=lambda k: order[k], reverse=True)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

