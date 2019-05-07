#Uses python3

import sys


def relax(u, v, v_idx, dist, cost):
    flag = False
    if dist[v] > dist[u] + cost[u][v_idx]:
        dist[v] = dist[u] + cost[u][v_idx]
        flag = True
    return flag, dist


def bellman_ford(adj, cost):
    len_adj = len(adj)
    dist = [-1]*len_adj
    dist[0] = 0

    for _ in range(len_adj):
        for u in range(len_adj):
            for v_idx, v in enumerate(adj[u]):
                flag, dist = relax(u, v, v_idx, dist, cost)

    return dist


def negative_cycle(adj, cost):
    dist = bellman_ford(adj, cost)

    for u in range(len(adj)):
        for v_idx, v in enumerate(adj[u]):
            flag, dist = relax(u, v, v_idx, dist, cost)
            if flag:
                return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
