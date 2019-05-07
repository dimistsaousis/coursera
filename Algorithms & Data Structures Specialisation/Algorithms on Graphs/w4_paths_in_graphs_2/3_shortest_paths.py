"""
Task. Given an directed graph with possibly negative edge weights and with n vertices and m edges as well
as its vertex s, compute the length of shortest paths from s to all other vertices of the graph.

Input Format. A graph is given in the standard format.

Constraints. 1 ≤ n ≤ 10^3, 0 ≤ m ≤ 10^4, 1 ≤ s ≤ n, edge weights are integers of absolute value at most
10^9

Output Format. For all vertices i from 1 to n output the following on a separate line:
• “*”, if there is no path from s to u;
• “-”, if there is a path from s to u, but there is no shortest path from s to u (that is, the distance
from s to u is −∞);
• the length of a shortest path otherwise.

Time Limits. C: 2 sec, C++: 2 sec, Java: 3 sec, Python: 10 sec. C#: 3 sec, Haskell: 4 sec, JavaScript:
10 sec, Ruby: 10 sec, Scala: 6 sec.

Memory Limit. 512Mb.
"""

import sys
import queue


def relax(u, v, v_idx, distance, cost, prev):
    flag = False
    if distance[v] > distance[u] + cost[u][v_idx]:
        distance[v] = distance[u] + cost[u][v_idx]
        prev[v] = u
        flag = True
    return flag, distance, prev


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


def shortest_path(adj, cost, s, distance, reachable, shortest):
    distance, reachable, shortest = bellman_ford(adj, cost, s, distance, reachable, shortest)
    reachable = [0 if d == float('inf') else 1 for d in distance]

    return distance, reachable, shortest


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
    s = data[0]
    s -= 1
    dist = [float('inf')] * n
    reach = [0] * n
    short = [1] * n
    dist, reach, short = shortest_path(adj_, cost_, s, dist, reach, short)
    for x in range(n):
        if reach[x] == 0:
            print('*')
        elif short[x] == 0:
            print('-')
        else:
            print(dist[x])

