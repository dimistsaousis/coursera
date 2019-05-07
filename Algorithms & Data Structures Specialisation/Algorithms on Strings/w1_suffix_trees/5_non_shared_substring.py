"""
Task. Find the shortest substring of one string that does not appear in another string.

Input Format. Strings Text1 and Text2.

Constraints. 1 ≤ |Text1|, |Text2| ≤ 2 000; strings have equal length (|Text1| = |Text2|), are not equal
(Text1 ̸= Text2), and contain symbols A, C, G, T only.

Output Format. The shortest (non-empty) substring of Text1 that does not appear in Text2. (Multiple
solutions may exist, in which case you may return any one.)

"""

import sys
import threading
sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


def max_substring(text_1, text_2):
    n_text_1 = len(text_1)
    n_text_2 = len(text_2)
    n = min(n_text_1, n_text_2)
    high = n
    low = 0
    while high-low > 1:
        mid = (high+low)//2
        if text_1[:mid] == text_2[:mid]:
            low = mid
        else:
            high = mid
    return high if text_1[:high] == text_2[:high] else low


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

    def empty(self):
        return len(self.dic) == 0

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
    def __init__(self, start=None, size=None, parent=None):
        self.parent = parent
        self.children = Children()
        self.start = start
        self.size = size
        self.only_left_leafs = None

    def add_child(self, start, size):
        new_node = Node(start, size, parent=self)
        return self.children.add(new_node)

    def edge(self, text, size=-1):
        size = self.size if size == -1 else size
        return text[self.start:self.start+size]

    def split(self, k):
        if 0 < k < self.size:
            new_node = Node(self.start+k, self.size-k, parent=self)
            new_node.inherit_children(self)
            self.size = k
            self.children.add(new_node)

    def inherit_children(self, node):
        self.children = node.children.copy()
        for v in self.children.values():
            v.parent = self
        node.children.reset()

    def leaf(self):
        return self.children.empty()

    def left_leaf(self, text):
        return "#" in self.edge(text)


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

    return tree_root


def has_all_left_leafs(node, text):
    if node.only_left_leafs is False:
        return False
    elif node.only_left_leafs is True:
        return True
    else:
        for current_node in node.children.values():
            if current_node.only_left_leafs is False:
                node.only_left_leafs = False
                return False
            elif current_node.only_left_leafs is None:
                if has_all_left_leafs(current_node, text) is False:
                    node.only_left_leafs = False
                    return False
    node.only_left_leafs = True
    return True


def get_all_left_leafs(tree_root, text):
    result = []
    q = Queue()
    for c in tree_root.children.values():
        q.add(c)

    while not q.empty():
        current_node = q.next()
        if current_node.leaf():
            edge = current_node.edge(text)
            if '#' in edge:
                current_node.only_left_leafs = True
                if not edge[0] == '#':
                    result.append(current_node)
            else:
                current_node.only_left_leafs = False
        else:
            for c in current_node.children.values():
                q.add(c)

    return result


def recreate_path_by_only_using_first_letter_of_the_leaf(leaf, text):
    result = leaf.edge(text)[0]
    node = leaf
    while node.parent is not None:
        node = node.parent
        if node.parent is not None:
            if has_all_left_leafs(node, text):
                result = node.edge(text)
            else:
                result = node.edge(text) + result
    return result


def pick_the_smallest(leafs, text):
    result = text
    for leaf in leafs:
        temp = recreate_path_by_only_using_first_letter_of_the_leaf(leaf, text)
        if len(result) > len(temp):
            result = temp
    return result


def solve(t1, t2):
    text = t1+"#"+t2+'$'
    tree_root = build_suffix_tree(text)
    leafs = get_all_left_leafs(tree_root, text)
    result = pick_the_smallest(leafs, text)
    return result


def main():
    text_1 = sys.stdin.readline().strip()
    text_2 = sys.stdin.readline().strip()
    ans = solve(text_1, text_2)
    sys.stdout.write(ans + '\n')


if __name__ == '__main__':
    threading.Thread(target=main).start()
