# Uses python3
import sys


def get_change(m):
    d = {1: 1, 2: 2, 3:1, 4:1}

    for i in range(5, m+1):
        d1 = d[i-1]+1
        d2 = d[i-3]+1
        d3 = d[i-4]+1
        d[i] = min(d1, d2, d3)

    return d[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
