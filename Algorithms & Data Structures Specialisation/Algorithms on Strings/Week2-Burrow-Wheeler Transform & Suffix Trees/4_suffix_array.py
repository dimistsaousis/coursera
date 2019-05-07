"""
Task. Construct the suffix array of a string.

Input Format. A string Text ending with a “$” symbol.

Constraints. 1 ≤ |Text(Text)| ≤ 104 ; except for the last symbol, Text contains symbols A, C, G, T only.

Output Format. SuffixArray(Text), that is, the list of starting positions (0-based) of sorted suffixes separated
by spaces.
"""


def build_suffix_array(t):
    """
    Build suffix array of the string text and
    return a list result of the same length as the text
    such that the value result[i] is the index (0-based)
    in text where the i-th lexicographically smallest
    suffix of text starts.
    """
    res = []
    n = len(t)
    for i in range(n):
        res.append(t[i:])

    return sorted(res)


if __name__ == '__main__':
    text = input().strip()
    print(" ".join(map(str, build_suffix_array(text))))
