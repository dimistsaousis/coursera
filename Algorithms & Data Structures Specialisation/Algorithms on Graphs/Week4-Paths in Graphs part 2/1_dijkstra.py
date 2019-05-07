"""
Task. Given an directed graph with positive edge weights and with n vertices and m edges as well as two
vertices u and v, compute the weight of a shortest path between u and v (that is, the minimum total
weight of a path from u to v).

Input Format. A graph is given in the standard format. The next line contains two vertices u and v.
Constraints. 1 ≤ n ≤ 103 , 0 ≤ m ≤ 105 , u 6= v, 1 ≤ u, v ≤ n, edge weights are non-negative integers not exceeding
10^3.

Output Format. Output the minimum weight of a path from u to v, or −1 if there is no path.

Time Limits. C: 2 sec, C++: 2 sec, Java: 3 sec, Python: 10 sec. C#: 3 sec, Haskell: 4 sec, JavaScript:
10 sec, Ruby: 10 sec, Scala: 6 sec.

Memory Limit. 512Mb.
"""

import sys
import queue


def relax(u, v, v_idx, dist, cost):
    flag = False
    if dist[v] > dist[u] + cost[u][v_idx]:
        dist[v] = dist[u] + cost[u][v_idx]
        flag = True
    return flag, dist


def distance(adj_array, cost, s, t):
    number_of_vertices = len(adj_array)
    finished_vertices = [0]*number_of_vertices
    dist = [10**7]*number_of_vertices

    dist[s] = 0
    finished_vertices[s] = 0
    q = queue.PriorityQueue()
    for v in range(number_of_vertices):
        q.put((dist[v], v))

    while not q.empty():
        _, u = q.get()
        while finished_vertices[u] == 1 and not q.empty():
            _, u = q.get()

        if finished_vertices[u] != 1:
            finished_vertices[u] = 1
            for v_idx, v in enumerate(adj_array[u]):
                flag, dist = relax(u, v, v_idx, dist, cost)
                if flag:
                    q.put((dist[v], v))
    return -1 if dist[t] == 10**7 else dist[t]


if __name__ == '__main__':
    inp = sys.stdin.read()
    data = list(map(int, inp.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost_ = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost_[a - 1].append(w)
    s_, t_ = data[0] - 1, data[1] - 1
    print(distance(adj, cost_, s_, t_))
