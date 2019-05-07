"""
Task. Extend TrieMatching algorithm so that it handles correctly cases when one of the patterns is a
prefix of another one.

Input Format. The first line of the input contains a string Text, the second line contains an integer 𝑛,
each of the following 𝑛 lines contains a pattern from Patterns = {𝑝1, . . . , 𝑝𝑛}.

Constraints. 1 ≤ |Text| ≤ 10 000; 1 ≤ 𝑛 ≤ 5 000; 1 ≤ |𝑝𝑖 | ≤ 100 for all 1 ≤ 𝑖 ≤ 𝑛; all strings contain only
symbols A, C, G, T; it can be the case that 𝑝𝑖 is a prefix of 𝑝𝑗 for some 𝑖, 𝑗.

Output Format. All starting positions in Text where a string from Patterns appears as a substring in
increasing order (assuming that Text is a 0-based array of symbols). If more than one pattern
appears starting at position 𝑖, output 𝑖 once.
"""

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


def solve (text, patterns):
    trie = build_trie(patterns)
    results = []
    for i in range(len(text)):
        count = prefix_trie_matching(text[i:], trie)
        if count > 0:
            results.append(i)

    return results


if __name__ == '__main__':
    txt = input().strip()
    n = int(input().strip())
    patt = []
    for _ in range(n):
        patt += [input().strip()]

    ans = solve(txt, patt)
