# Uses python3
import sys


def init_matrix(n, m):
    matrix = []
    for i in range(n+1):
        l = []
        for j in range(m+1):
            l.append(0)
        matrix.append(l)
    return matrix


def optimal_weight(W, w):
    wn = len(w)
    v = init_matrix(W, wn)
    for i in range(W+1):
        for j in range(wn+1):
            if i != 0 and j != 0:
                if w[j-1] > i:
                    v[i][j] = v[i][j-1]
                else:
                    d1 = v[i - w[j-1]][j - 1] + w[j-1]
                    d2 = v[i][j - 1]
                    v[i][j] = max(d1, d2)
    return v[W][wn]


if __name__ == '__main__':
    # W = 10
    # w = [1, 4, 8]
    # print(optimal_weight(W,w))
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
