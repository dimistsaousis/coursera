# python3
import sys


class Queue:
    def __init__(self):
        self._array = []

    def next(self):
        return self._array.pop(0)

    def add(self, v):
        self._array.append(v)

    def empty(self):
        return len(self._array) == 0


class Children:
    def __init__(self):
        self.idx_list = []
        self.dic = dict()

    def add(self, idx, node):
        if idx in self.idx_list:
            idx_pos = self.idx_list.index(idx)
            self.idx_list.pop(idx_pos)
        self.dic[idx] = node
        self.idx_list.append(idx)

    def get(self, idx):
        return self.dic[idx]


class Node:
    def __init__(self, parent=None, string_depth=None, edge_start=None, edge_end=None):
        self.parent = parent
        self.children = Children()
        self.string_depth = string_depth
        self.edge_start = edge_start
        self.edge_end = edge_end


def suffix_array_to_suffix_tree(suffix_array, lcp_array, text):
    root_node = Node(string_depth=0, edge_start=-1, edge_end=-1)
    lcp_prev = 0
    current_node = root_node

    for i in range(len(text)):
        suffix = suffix_array[i]
        while current_node.string_depth > lcp_prev:
            current_node = current_node.parent
        if current_node.string_depth == lcp_prev:
            current_node = create_new_leaf(current_node, text, suffix)
        else:
            edge_start = suffix_array[i-1] + current_node.string_depth
            offset = lcp_prev - current_node.string_depth
            mid_node = break_edge(current_node, text, edge_start, offset)
            current_node = create_new_leaf(mid_node, text, suffix)
        if i < len(text)-1:
            lcp_prev = lcp_array[i]

    return root_node


def create_new_leaf(node, text, suffix):
    leaf = Node(parent=node, string_depth=len(text)-suffix, edge_start=suffix+node.string_depth, edge_end=len(text)-1)
    node.children.add(text[leaf.edge_start], leaf)
    return leaf


def break_edge(node, text, start, offset):
    start_char = text[start]
    mid_char = text[start+offset]
    mid_node = Node(parent=node, string_depth=node.string_depth+offset, edge_start=start, edge_end=start+offset-1)
    mid_node.children.add(mid_char, node.children.get(start_char))
    start_char_node = node.children.get(start_char)
    start_char_node.parent = mid_node
    start_char_node.edge_start = start_char_node.edge_start+offset
    node.children.add(start_char, mid_node)
    return mid_node


class Stack:
    def __init__(self):
        self.arr = []

    def add(self, n):
        self.arr.append(n)

    def next(self):
        return self.arr.pop(-1)

    def empty(self):
        return len(self.arr) == 0


def output_edges(root_node):
    stack = Stack()
    n = len(root_node.children.idx_list)

    for i in range(n-1, -1, -1):
        idx = root_node.children.idx_list[i]
        c = root_node.children.get(idx)
        stack.add(c)

    while not stack.empty():
        node = stack.next()
        print("%d %d" % (node.edge_start, node.edge_end + 1))
        n = len(node.children.idx_list)
        for i in range(n-1, -1, -1):
            idx = node.children.idx_list[i]
            c = node.children.get(idx)
            stack.add(c)


if __name__ == '__main__':
    input_text = sys.stdin.readline().strip()
    sa = list(map(int, sys.stdin.readline().strip().split()))
    lcp = list(map(int, sys.stdin.readline().strip().split()))
    print(input_text)
    tree_root = suffix_array_to_suffix_tree(sa, lcp, input_text)
    output_edges(tree_root)
