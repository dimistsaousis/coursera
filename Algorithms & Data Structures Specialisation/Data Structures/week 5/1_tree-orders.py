# python3

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

