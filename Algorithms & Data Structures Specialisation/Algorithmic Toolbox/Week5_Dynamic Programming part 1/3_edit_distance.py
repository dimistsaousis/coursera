"""
Task. The goal of this problem is to implement the algorithm for computing the edit distance between two
strings.

Input Format. Each of the two lines of the input contains a string consisting of lower case latin letters.

Constraints. The length of both strings is at least 1 and at most 100.

Output Format. Output the edit distance between the given two strings.
"""


def edit_distance(s, t):
    n_s = len(s)
    n_t = len(t)

    ed = init_matrix(n_s, n_t)

    for i in range(n_s+1):
        for j in range(n_t+1):
            if i == 0:
                ed[i][j] = j
            elif j == 0:
                ed[i][j] = i
            else:
                diff = 0 if s[i-1] == t[j-1] else 1
                ed1 = ed[i][j-1]+1
                ed2 = ed[i-1][j]+1
                ed3 = ed[i-1][j-1] + diff
                ed[i][j] = min(ed1, ed2, ed3)
    return ed[n_s][n_t]


def init_matrix(n, m):
    matrix = []
    for i in range(n+1):
        l = []
        for j in range(m+1):
            l.append(0)
        matrix.append(l)
    return matrix


if __name__ == "__main__":
    print(edit_distance(input(), input()))
