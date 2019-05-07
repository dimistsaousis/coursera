#!/usr/bin/python3
import sys
import threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


def is_bst(node, min_value, max_value, tree):
    if node == -1:
        return True
    node_value = tree[node][0]
    if (min_value and node_value < min_value) or (max_value and node_value >= max_value):
        return False
    left = tree[node][1]
    right = tree[node][2]
    return is_bst(left, min_value, tree[node][0], tree) and is_bst(right, tree[node][0], max_value, tree)


def is_binary_search_tree(tree):
    if len(tree) == 0:
        return True
    left = tree[0][1]
    right = tree[0][2]
    return is_bst(left, None, tree[0][0], tree) and is_bst(right, tree[0][0], None, tree)


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if is_binary_search_tree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")

#
# if __name__ == '__main__':
#     main()


threading.Thread(target=main).start()
