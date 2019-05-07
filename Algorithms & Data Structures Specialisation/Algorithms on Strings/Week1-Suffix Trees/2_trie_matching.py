"""
Task. Implement TrieMatching algorithm.

Input Format. The first line of the input contains a string Text, the second line contains an integer 𝑛,
each of the following 𝑛 lines contains a pattern from Patterns = {𝑝1, . . . , 𝑝𝑛}.

Constraints. 1 ≤ |Text| ≤ 10 000; 1 ≤ 𝑛 ≤ 5 000; 1 ≤ |𝑝𝑖 | ≤ 100 for all 1 ≤ 𝑖 ≤ 𝑛; all strings contain only
symbols A, C, G, T; no 𝑝𝑖 is a prefix of 𝑝𝑗 for all 1 ≤ 𝑖 ̸= 𝑗 ≤ 𝑛.

Output Format. All starting positions in Text where a string from Patterns appears as a substring in
increasing order (assuming that Text is a 0-based array of symbols).
"""


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
            if u[symbol] not in trie or len(trie[u[symbol]]) == 0:
                return True
            u = trie[u[symbol]]
            if next_symbol == text_len:
                return False
            symbol = text[next_symbol]
            next_symbol += 1
        else:
            return False


def solve (text, patterns):
    trie = build_trie(patterns)
    results = []
    for i in range(len(text)):
        flag = prefix_trie_matching(text[i:], trie)
        if flag:
            results.append(i)

    return results


if __name__ == '__main__':
    txt = input().strip()
    size_patterns = int(input().strip ())
    patt = []
    for _ in range(size_patterns):
        patt += [input().strip()]

    ans = solve(txt, patt)

