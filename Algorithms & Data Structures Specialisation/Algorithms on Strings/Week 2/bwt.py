# python3
import sys


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
    t = sys.stdin.readline().strip()
    print(bwt(t))
