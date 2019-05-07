"""
Task. You are given a description of a rooted tree. Your task is to compute and output its height. Recall
that the height of a (rooted) tree is the maximum depth of a node, or the maximum distance from a
leaf to the root. You are given an arbitrary tree, not necessarily a binary tree.

Input Format. The first line contains the number of nodes 𝑛. The second line contains 𝑛 integer numbers
from −1 to 𝑛 − 1 — parents of nodes. If the 𝑖-th one of them (0 ≤ 𝑖 ≤ 𝑛 − 1) is −1, node 𝑖 is the root,
otherwise it’s 0-based index of the parent of 𝑖-th node. It is guaranteed that there is exactly one root.
It is guaranteed that the input represents a tree.

Constraints. 1 ≤ 𝑛 ≤ 105.

Output Format. Output the height of the tree.
"""
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, nxt in enumerate(text):
        if nxt in "([{":
            opening_brackets_stack.append(Bracket(nxt, i))

        elif nxt in ")]}":
            if opening_brackets_stack:
                previous = opening_brackets_stack.pop().char
                if nxt == ')' and previous != '(':
                    return i+1
                if nxt == ']' and previous != '[':
                    return i+1
                if nxt == '}' and previous != '{':
                    return i+1
            else:
                return i+1

    if opening_brackets_stack:
        return opening_brackets_stack.pop().position+1
    else:
        return 'Success'


def main():
    # text = 'foo(bar[i);'
    # print(find_mismatch(text))
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
