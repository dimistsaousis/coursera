"""
Task. Construct the Burrows–Wheeler transform of a string.

Input Format. A string Text ending with a “$” symbol.

Constraints. 1 ≤ |Text| ≤ 1 000; except for the last symbol, Text contains symbols A, C, G, T only.

Output Format. BWT(Text).
"""


def bwt(text):
    n = len(text)
    cycle_matrix = []
    s = text
    for _ in range(n):
        cycle_matrix.append(s)
        s = s[-1]+s[:-1]
    cycle_matrix = sorted(cycle_matrix)
    res = ""
    for k in cycle_matrix:
        res = res + k[-1]
    return res


if __name__ == '__main__':
    t = input().strip()
    print(bwt(t))
