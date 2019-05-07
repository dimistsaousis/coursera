"""
Task. Construct a suffix tree from the suffix array and LCP array of a string.

Input Format. The first line contains a string Text ending with a “$” symbol, the second line contains
SuffixArray(Text) as a list of |Text| integers separated by spaces, the last line contains LCP(Text) as
a list of |Text| − 1 integers separated by spaces.

Constraints. 1 ≤ |Text(Text)| ≤ 2 · 105; except for the last symbol, Text contains symbols A, C, G, T only.

Output Format. The output format in this problem differs from the output format in the problem “Suffix
Tree” from the Programming Assignment 2 and is somewhat tricky. It is because this problem is
harder: the input string can be longer, so it would take too long to output all the edge labels directly
and compare them with the correct ones, as their combined length can be Θ(|Text| 2 ), which is too much when the
Text can be as long as 200 000 characters. Output the 𝑇 𝑒𝑥𝑡 from the input on the first line. Then output all the
edges of the suffix tree in a specific order (see below), each on its own line. Output each edge as a pair of integers
(start, end), where start is the position in Text corresponding to the start of the edge label substring
in the Text and end is the position right after the end of the edge label in the Text. Note that start
must be a valid position in the Text, that is, 0 ≤ 𝑠𝑡𝑎𝑟𝑡 ≤ |Text| − 1, and end must be between 1 and
|Text| inclusive. Substring Text[start..end − 1] must be equal to the edge label of the corresponding
edge. For example, if Text = “ACACAA$” and the edge label is “CA”, you can output this edge either
as (1, 3) corresponding to Text[1..2] = “CA” or as (3, 5) corresponding to Text[3..4] = “CA” — both
variants will be accepted.

The order of the edges is important here — if you output all the correct edges in the wrong order, your
solution will not be accepted. However, you don’t need to construct this order yourself if you
write in C++, Java or Python3, because it is implemented for you in the starter files.
Output all the edges in the order of sorted suffixes: first, take the leaf of the suffix tree corresponding
to the smallest suffix of Text and output all the edges on the path from the root to this leaf. Then
take the leaf corresponding to the second smallest suffix of Text and output all the edges on the path
from the root to this leaf except for those edges which were printed before. Then take the leaf
corresponding to the third smallest suffix, fourth smallest suffix and so on. Print each edge only once
— as a part of the path corresponding to the smallest suffix of Text where this edge appears. This way,
you will only output 𝑂(|Text|) integers. See the examples below for clarification.

"""


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
    input_text = input().strip()
    sa = list(map(int, input().strip().split()))
    lcp = list(map(int, input().strip().split()))
    print(input_text)
    tree_root = suffix_array_to_suffix_tree(sa, lcp, input_text)
    output_edges(tree_root)
