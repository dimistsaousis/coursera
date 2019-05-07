"""
Task. Given three sequences 𝐴 = (𝑎1, 𝑎2, . . . , 𝑎𝑛), 𝐵 = (𝑏1, 𝑏2, . . . , 𝑏𝑚), and 𝐶 = (𝑐1, 𝑐2, . . . , 𝑐𝑙), find the
length of their longest common sub sequence, i.e., the largest non-negative integer 𝑝 such that there
exist indices 1 ≤ 𝑖1 < 𝑖2 < · · · < 𝑖𝑝 ≤ 𝑛, 1 ≤ 𝑗1 < 𝑗2 < · · · < 𝑗𝑝 ≤ 𝑚, 1 ≤ 𝑘1 < 𝑘2 < · · · < 𝑘𝑝 ≤ 𝑙 such
that 𝑎𝑖1 = 𝑏𝑗1 = 𝑐𝑘1, . . . , 𝑎𝑖𝑝 = 𝑏𝑗𝑝 = 𝑐𝑘𝑝

Input Format.
First line: 𝑛.
Second line: 𝑎1, 𝑎2, . . . , 𝑎𝑛.
Third line: 𝑚.
Fourth line: 𝑏1, 𝑏2, . . . , 𝑏𝑚.
Fifth line: 𝑙.
Sixth line: 𝑐1, 𝑐2, . . . , 𝑐𝑙.

Constraints. 1 ≤ 𝑛, 𝑚, 𝑙 ≤ 100; −109 < 𝑎𝑖 , 𝑏𝑖 , 𝑐𝑖 < 109.

Output Format. Output 𝑝.
"""


def get_longest_common_sub_sequence3d(seq_a, seq_b, sec_c):
    len_a = len(seq_a)
    len_b = len(seq_b)
    len_c = len(sec_c)
    x = init_matrix3d(len_a, len_b, len_c)

    for i in range(len_a+1):
        for j in range(len_b+1):
            for k in range(len_c+1):
                if i == 0 or j == 0 or k == 0:
                    x[i][j][k] = 0
                else:
                    diff = 1 if seq_a[i - 1] == seq_b[j - 1] == sec_c[k - 1] else 0
                    x[i][j][k] = max(x[i-1][j][k],
                                     x[i-1][j-1][k],
                                     x[i-1][j][k-1],
                                     x[i][j-1][k],
                                     x[i][j-1][k-1],
                                     x[i][j][k-1],
                                     x[i-1][j-1][k-1]+diff)

    return x[len_a][len_b][len_c]


def init_matrix(n, m):
    matrix = []
    for i in range(n+1):
        l = []
        for j in range(m+1):
            l.append(0)
        matrix.append(l)
    return matrix


def init_matrix3d(n1, n2, n3):
    matrix1 = []
    for i in range(n1+1):
        matrix2 = []
        for j in range(n2+1):
            matrix3 = []
            for k in range(n3+1):
                matrix3.append(0)
            matrix2.append(matrix3)
        matrix1.append(matrix2)
    return matrix1


if __name__ == '__main__':
    data = list(map(int, input().split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(get_longest_common_sub_sequence3d(a, b, c))
