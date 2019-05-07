"""
Task. Given two sequences 𝐴 = (𝑎1, 𝑎2, . . . , 𝑎𝑛) and 𝐵 = (𝑏1, 𝑏2, . . . , 𝑏𝑚), find the length of their longest
common subsequence, i
.e., the largest non-negative integer 𝑝 such that there exist indices:
 1 ≤ 𝑖1 <𝑖2 < · · · < 𝑖𝑝 ≤ 𝑛 and
 1 ≤ 𝑗1 < 𝑗2 < · · · < 𝑗𝑝 ≤ 𝑚
 such that 𝑎𝑖1 = 𝑏𝑗1, . . . , 𝑎𝑖𝑝 = 𝑏𝑗𝑝.

Input Format. First line: 𝑛. Second line: 𝑎1, 𝑎2, . . . , 𝑎𝑛. Third line: 𝑚. Fourth line: 𝑏1, 𝑏2, . . . , 𝑏𝑚.

Constraints. 1 ≤ 𝑛, 𝑚 ≤ 100; −109 < 𝑎𝑖 , 𝑏𝑖 < 109.

Output Format. Output 𝑝.
"""


def get_longest_common_sub_sequence(seq_a, seq_b):
    len_a = len(seq_a)
    len_b = len(seq_b)

    x = init_matrix(len_a, len_b)

    for i in range(len_a+1):
        for j in range(len_b+1):
            if i == 0 or j == 0:
                x[i][j] = 0
            else:
                diff = 1 if seq_a[i - 1] == seq_b[j - 1] else 0
                x[i][j] = max(x[i][j-1], x[i-1][j], x[i-1][j-1]+diff)
    return x[len_a][len_b]


def init_matrix(rows, cols):
    matrix = []
    for i in range(rows + 1):
        l = []
        for j in range(cols + 1):
            l.append(0)
        matrix.append(l)
    return matrix


if __name__ == '__main__':
    data = list(map(int, input().split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(get_longest_common_sub_sequence(a, b))

