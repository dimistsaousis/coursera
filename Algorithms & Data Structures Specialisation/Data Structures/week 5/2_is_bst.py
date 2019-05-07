#!/usr/bin/python3

import sys
import threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


def in_order_traversal(n, result, tree):
    if n == -1:
        return result
    left = tree[n][1]
    right = tree[n][2]
    in_order_traversal(left, result, tree)
    result.append(tree[n][0])
    in_order_traversal(right, result, tree)
    return result


def is_binary_search_tree(tree):
    size_tree = len(tree)
    if size_tree == 0:
        return True
    result = in_order_traversal(0, [], tree)
    size = len(result)
    if size != size_tree:
        return False
    for i in range(1, size):
        if result[i] <= result[i-1]:
            return False
    return True


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if is_binary_search_tree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


# if __name__ == '__main__':
#     main

threading.Thread(target=main).start()
