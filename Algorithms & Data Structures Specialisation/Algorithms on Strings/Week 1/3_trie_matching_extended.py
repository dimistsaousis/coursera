# python3
import sys

NA = -1


class Node:
    def __init__(self, idx, end_of_pattern=False):
        self.node_idx = idx
        self.children = dict()
        self.end_of_pattern = end_of_pattern

    def add(self, edge_value, node):
        self.children[edge_value] = node

    def is_leaf(self):
        return not self.children


def build_trie(patterns):
    tree = Node(0)
    total_nodes = 1
    for pattern in patterns:
        current_node = tree
        for i, s in enumerate(pattern):
            if s in current_node.children:
                current_node = current_node.children[s]
            else:
                current_node.add(s, Node(total_nodes))
                current_node = current_node.children[s]
                total_nodes += 1
        current_node.end_of_pattern = True
    return tree


def prefix_trie_matching(text, trie):
    text_len = len(text)
    next_symbol = 1
    symbol = text[0]
    u = trie
    count = 0
    while True:
        if symbol in u.children:
            if u.children[symbol].is_leaf():
                count += 1
                return count
            if u.children[symbol].end_of_pattern:
                count += 1
            u = u.children[symbol]
            if next_symbol == text_len:
                return count
            symbol = text[next_symbol]
            next_symbol += 1
        else:
            return count


def solve (text, n, patterns):
    trie = build_trie(patterns)
    results = []
    for i in range(len(text)):
        count = prefix_trie_matching(text[i:], trie)
        if count > 0:
            results.append(i)

    return results


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    patterns = []
    for i in range(n):
        patterns += [sys.stdin.readline().strip()]

    ans = solve(text, n, patterns)

    sys.stdout.write(' '.join(map(str, ans)) + '\n')
