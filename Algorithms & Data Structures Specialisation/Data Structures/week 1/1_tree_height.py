# python3

import sys
import threading


def compute_height(n, parents):
    # Replace this code with a faster implementation
    nodes = [[] for _ in range(n)]

    head = -1
    for i, p in enumerate(parents):
        if p != -1:
            nodes[p].append(i)
        else:
            head = i

    return compute_node_height(head, nodes)+1


def compute_node_height(node, nodes):
    n = nodes[node]
    if len(n) == 0:
        return 0
    else:
        h = 0
        for n1 in n:
            h = max(h, compute_node_height(n1, nodes)+1)
        return h


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
