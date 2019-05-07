#Uses python3

import sys
import queue


def relax(u, v, v_idx, dist, cost, prev):
    flag = False
    if dist[v] > dist[u] + cost[u][v_idx]:
        dist[v] = dist[u] + cost[u][v_idx]
        prev[v] = u
        flag = True
    return flag, dist, prev


def bellman_ford(adj, cost, s, distance, reachable, shortest):
    len_adj = len(adj)
    prev = [None] * len_adj
    distance[s] = 0

    for itters in range(len_adj+2):
        for u in range(len_adj):
            for v_idx, v in enumerate(adj[u]):
                flag, distance, prev = relax(u, v, v_idx, distance, cost, prev)
                if shortest[v] == 0:
                    for neighbor in adj[v]:
                        shortest[neighbor] = 0
                if itters == len_adj and flag:
                    shortest[v] = 0
                    x = prev[v]
                    count = 0
                    while x is not None and x != v and count < len_adj:
                        shortest[x] = 0
                        x = prev[x]
                        count += 1
    return distance, reachable, shortest


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    distance, reachable, shortest = bellman_ford(adj, cost, s, distance, reachable, shortest)
    reachable = [0 if d == float('inf') else 1 for d in distance]

    return distance, reachable, shortest


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
    s = data[0]
    s -= 1
    distance = [float('inf')] * n
    reachable = [0] * n
    shortest = [1] * n
    distance, reachable, shortest = shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

