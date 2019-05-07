"""
Task. Given an directed graph with possibly negative edge weights and with n vertices and m edges, check
whether it contains a cycle of negative weight.
Input Format. A graph is given in the standard format.

Constraints. 1 ≤ n ≤ 10^3, 0 ≤ m ≤ 10^4 , edge weights are integers of absolute value at most 10^3.

Output Format. Output 1 if the graph contains a cycle of negative weight and 0 otherwise.

Time Limits. C: 2 sec, C++: 2 sec, Java: 3 sec, Python: 10 sec. C#: 3 sec, Haskell: 4 sec, JavaScript:
10 sec, Ruby: 10 sec, Scala: 6 sec.

Memory Limit. 512Mb.
"""

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
    inp = sys.stdin.read()
    data = list(map(int, inp.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj_ = [[] for _ in range(n)]
    cost_ = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj_[a - 1].append(b - 1)
        cost_[a - 1].append(w)
    print(negative_cycle(adj_, cost_))
