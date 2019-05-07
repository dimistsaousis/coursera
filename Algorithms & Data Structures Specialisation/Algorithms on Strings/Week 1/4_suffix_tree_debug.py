# python3
import sys


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


class Node:
    def __init__(self, start=None, size=None, text=None):
        self.children = dict()
        self.start = start
        self.size = size
        self.__c_id = 0
        self.text = text

    def add(self, start, size):
        self.children[self.__c_id] = Node(start, size, text=self.text)
        self.__c_id += 1
        return self.children[self.__c_id-1]

    def is_in(self, string, text):
        if len(string) == 0:
            return -1
        for k, v in self.children.items():
            if v.get(text)[0] == string[0]:
                return k
        return -1

    def get(self, text):
        return text[self.start:self.start+self.size]

    def split(self, string, text):
        edge = self.get(text)
        k = max_substring(edge, string)
        if k == 0:
            return k, self
        elif k == len(edge):
            return k, self
        else:
            # New Node
            new_edge_start = self.start+k
            new_edge_size = self.size-k
            new_node = Node(new_edge_start, new_edge_size, text=self.text)
            new_node.children = self.children
            new_node.__c_id = self.__c_id
            # End new node
            self.size = k
            self.reset_children()
            self.children[self.__c_id] = new_node
            self.__c_id += 1
            return k, self

    def reset_children(self):
        self.children = dict()
        self.__c_id = 0

    def __repr__(self):
        if self.start is not None:
            return self.get(self.text)
        else:
            return 'root'


def build_suffix_tree(text):
    """
    Build a suffix tree of the string text and return a list
    with all of the labels of its edges (the corresponding
    substrings of the text) in any order.
    """
    tree = Node(text=text)
    n_text = len(text)

    for start in range(n_text):
        c_node = tree
        i = c_node.is_in(text[start:], text)
        while i != -1:
            c_node = c_node.children[i]
            new_start, c_node = c_node.split(text[start:], text)
            start += new_start
            i = c_node.is_in(text[start:], text)

        if i != n_text:
            c_node.add(start, n_text-start)

    return bfs(tree, text)


def bfs(tree, text):
    res = []
    q = Queue()
    for c in tree.children.values():
        q.add(c)

    while not q.empty():
        child = q.next()
        # res.append(child.edge)
        res.append(child.get(text))
        for c in child.children.values():
            q.add(c)

    return res


if __name__ == '__main__':
    # text = sys.stdin.readline().strip()
    input_text = 'ATAAATG$'
    result = build_suffix_tree(input_text)
    print("\n".join(result))
