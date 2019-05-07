#Uses python3

import sys
import queue


def relax(u, v, v_idx, dist, cost):
    flag = False
    if dist[v] > dist[u] + cost[u][v_idx]:
        dist[v] = dist[u] + cost[u][v_idx]
        flag = True
    return flag, dist


def distance(adj, cost, s, t):
    number_of_vertices = len(adj)
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
            for v_idx, v in enumerate(adj[u]):
                flag, dist = relax(u, v, v_idx, dist, cost)
                if flag:
                    q.put((dist[v], v))
    return -1 if dist[t] == 10**7 else dist[t]


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
