# python3
import sys


def find_pattern(pattern, text):
    len_p = len(pattern)
    len_t = len(text)
    s = pattern + "$" + text
    s = compute_prefix_function(s)
    result = []

    for i in range(len_p+1, len_p+len_t+1):
        if s[i] == len_p:
            result.append(i-2*len_p)

    return result


def compute_prefix_function(text):
    len_t = len(text)
    s = [0]*len_t
    s[0] = 0
    border = 0

    for i in range(1, len_t):
        while border > 0 and text[i] != text[border]:
            border = s[border-1]
        if text[i] == text[border]:
            border += 1
        else:
            border = 0
        s[i] = border

    return s


if __name__ == '__main__':
    p = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    res = find_pattern(p, t)
    print(" ".join(map(str, res)))

