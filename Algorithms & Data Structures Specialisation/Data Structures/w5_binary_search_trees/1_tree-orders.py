"""
Task. You are given a rooted binary tree. Build and output its in-order, pre-order and post-order traversals.
Input Format. The first line contains the number of vertices 𝑛. The vertices of the tree are numbered
from 0 to 𝑛 − 1. Vertex 0 is the root.
The next 𝑛 lines contain information about vertices 0, 1, ..., 𝑛−1 in order. Each of these lines contains
three integers 𝑘𝑒𝑦𝑖, 𝑙𝑒𝑓𝑡𝑖 and 𝑟𝑖𝑔ℎ𝑡𝑖 — 𝑘𝑒𝑦𝑖 is the key of the 𝑖-th vertex, 𝑙𝑒𝑓 𝑡𝑖 is the index of the left child of the
𝑖-th vertex, and 𝑟𝑖𝑔ℎ𝑡𝑖 is the index of the right child of the 𝑖-th vertex. If 𝑖 doesn’t have left or right child
(or both), the corresponding 𝑙𝑒𝑓 𝑡𝑖 or 𝑟𝑖𝑔ℎ𝑡𝑖 (or both) will be equal to −1.

Constraints. 1 ≤ 𝑛 ≤ 105 ; 0 ≤ 𝑘𝑒𝑦𝑖 ≤ 109 ; −1 ≤ 𝑙𝑒𝑓 𝑡𝑖, 𝑟𝑖𝑔ℎ𝑡𝑖 ≤ 𝑛 − 1. It is guaranteed that the input represents a
valid binary tree. In particular, if 𝑙𝑒𝑓 𝑡𝑖 ̸= −1 and 𝑟𝑖𝑔ℎ𝑡𝑖 ̸= −1, then 𝑙𝑒𝑓 𝑡𝑖 ̸= 𝑟𝑖𝑔ℎ𝑡𝑖. Also, a vertex cannot be a child
of two different vertices. Also, each vertex is a descendant of the root vertex.

Output Format. Print three lines. The first line should contain the keys of the vertices in the in-order
traversal of the tree. The second line should contain the keys of the vertices in the pre-order traversal
of the tree. The third line should contain the keys of the vertices in the post-order traversal of the tree.
"""

import sys
import threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:
    def __init__(self):
        self.n = None
        self.key = []
        self.left = []
        self.right = []
        self.result = []

    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for _ in range(self.n)]
        self.left = [0 for _ in range(self.n)]
        self.right = [0 for _ in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def in_order(self):
        self.result = []
        self.in_order_traversal(0)
        return self.result

    def in_order_traversal(self, n):
        if n == -1:
            return
        left = self.left[n]
        right = self.right[n]
        self.in_order_traversal(left)
        self.result.append(self.key[n])
        self.in_order_traversal(right)

    def pre_order(self):
        self.result = []
        self.pre_order_traversal(0)
        return self.result

    def pre_order_traversal(self, n):
        if n == -1:
            return
        self.result.append(self.key[n])
        left = self.left[n]
        right = self.right[n]
        self.pre_order_traversal(left)
        self.pre_order_traversal(right)

    def post_order(self):
        self.result = []
        self.post_order_traversal(0)
        return self.result

    def post_order_traversal(self, n):
        if n == -1:
            return
        left = self.left[n]
        right = self.right[n]
        self.post_order_traversal(left)
        self.post_order_traversal(right)
        self.result.append(self.key[n])


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.in_order()))
    print(" ".join(str(x) for x in tree.pre_order()))
    print(" ".join(str(x) for x in tree.post_order()))


# if __name__ == '__main__':
#     main()

threading.Thread(target=main).start()

