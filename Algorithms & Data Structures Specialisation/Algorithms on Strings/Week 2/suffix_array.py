# python3
import sys


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
    # suffix_array = [i for i in range(n)]
    #
    # return sorted(suffix_array, key=lambda x: res[x])


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(" ".join(map(str, build_suffix_array(text))))
