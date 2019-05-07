"""
Task. Construct the suffix tree of a string.

Input Format. A string Text ending with a “$” symbol.

Constraints. 1 ≤ |Text| ≤ 5 000; except for the last symbol, Text contains symbols A, C, G, T only.

Output Format. The strings labeling the edges of SuffixTree(Text) in any order.
"""


def max_substring(text_1, text_2):
    n_text_1 = len(text_1)
    n_text_2 = len(text_2)
    n = min(n_text_1, n_text_2)
    for i in range(n+1):
        if text_1[:i] != text_2[:i]:
            return i-1
    return n


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
        self.dic = dict()
        self.__id = 0

    def add(self, child):
        self.dic[self.__id] = child
        self.__id += 1
        return child

    def reset(self):
        self.__id = 0
        self.dic = dict()

    def get_node(self, idx):
        return self.dic[idx]

    def find(self, string, text):
        for k, v in self.items():
            if v.edge(text, 1) == string[0]:
                return k
        return -1

    def items(self):
        return self.dic.items()

    def values(self):
        return self.dic.values()

    def copy(self):
        c = Children()
        c.dic = self.dic.copy()
        c.__id = self.__id
        return c


class Node:
    def __init__(self, start=None, size=None):
        self.children = Children()
        self.start = start
        self.size = size

    def add_child(self, start, size):
        new_node = Node(start, size)
        return self.children.add(new_node)

    def edge(self, text, size=-1):
        size = self.size if size == -1 else size
        return text[self.start:self.start+size]

    def split(self, k):
        if 0 < k < self.size:
            new_node = Node(self.start+k, self.size-k)
            new_node.inherit_children(self)
            self.size = k
            self.children.add(new_node)

    def inherit_children(self, node):
        self.children = node.children.copy()
        node.children.reset()


def build_suffix_tree(text):
    tree_root = Node()
    n = len(text)
    for start in range(n):
        current_node = tree_root
        child_index = current_node.children.find(text[start:], text)
        while child_index != -1:
            current_node = current_node.children.get_node(child_index)
            k = max_substring(text[start:], current_node.edge(text))
            current_node.split(k)

            start += k
            child_index = current_node.children.find(text[start:], text)

        if child_index != n:
            current_node.add_child(start, n-start)

    return breadth_first_edges(tree_root, text)


def breadth_first_edges(tree_root, text):
    result = []
    q = Queue()
    for c in tree_root.children.values():
        q.add(c)

    while not q.empty():
        current_node = q.next()
        result.append(current_node.edge(text))

        for c in current_node.children.values():
            q.add(c)

    return result


if __name__ == '__main__':
    input_text = input().strip()
    res = build_suffix_tree(input_text)
    print("\n".join(res))
