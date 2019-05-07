"""
Task. Construct a trie from a collection of patterns.

Input Format. An integer 𝑛 and a collection of strings Patterns = {𝑝1, . . . , 𝑝𝑛} (each string is given on a
separate line).

Constraints. 1 ≤ 𝑛 ≤ 100; 1 ≤ |𝑝𝑖 | ≤ 100 for all 1 ≤ 𝑖 ≤ 𝑛; 𝑝𝑖 ’s contain only symbols A, C, G, T; no 𝑝𝑖 is a prefix
of 𝑝𝑗 for all 1 ≤ 𝑖 ̸= 𝑗 ≤ 𝑛.

Output Format. The adjacency list corresponding to Trie(Patterns), in the following format. If
Trie(Patterns) has 𝑛 nodes, first label the root with 0 and then label the remaining nodes with the
integers 1 through 𝑛−1 in any order you like. Each edge of the adjacency list of Trie(Patterns) will be
encoded by a triple: the first two members of the triple must be the integers 𝑖, 𝑗 labeling the initial and
terminal nodes of the edge, respectively; the third member of the triple must be the symbol 𝑐 labeling
the edge; output each such triple in the format u->v:c (with no spaces) on a separate line.
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


if __name__ == '__main__':
    pat = input().split()[1:]
    res = build_trie(pat)
    for node in res:
        for c in res[node]:
            print("{}->{}:{}".format(node, res[node][c], c))
