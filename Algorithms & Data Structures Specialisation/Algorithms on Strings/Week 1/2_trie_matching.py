# python3
import sys


def build_trie(patterns):
    tree = dict()
    current_node = tree
    edge_count = 1
    for i, s in enumerate(patterns[0]):
        current_node[i] = {s: edge_count}
        edge_count += 1

    for pattern in patterns[1:]:
        current_node = tree[0]
        for i, s in enumerate(pattern):
            if s in current_node:
                edge = current_node[s]
                current_node = tree[edge]
            else:
                current_node[s] = edge_count
                tree[edge_count] = {}
                current_node = tree[edge_count]
                edge_count += 1
    return tree


def prefix_trie_matching(text, trie):
    text_len = len(text)
    next_symbol = 1
    symbol = text[0]
    u = trie[0]
    while True:
        if symbol in u:
            # LEAF
            if u[symbol] not in trie or len(trie[u[symbol]]) == 0:
                return True
            u = trie[u[symbol]]
            if next_symbol == text_len:
                return False
            symbol = text[next_symbol]
            next_symbol += 1
        else:
            return False


def solve (text, n, patterns):
    trie = build_trie(patterns)
    results = []
    for i in range(len(text)):
        flag = prefix_trie_matching(text[i:], trie)
        if flag:
            results.append(i)

    return results


if __name__ == '__main__':
    text = sys.stdin.readline ().strip ()
    n = int (sys.stdin.readline ().strip ())
    patterns = []
    for i in range (n):
        patterns += [sys.stdin.readline ().strip ()]

    ans = solve (text, n, patterns)

    sys.stdout.write (' '.join (map (str, ans)) + '\n')

