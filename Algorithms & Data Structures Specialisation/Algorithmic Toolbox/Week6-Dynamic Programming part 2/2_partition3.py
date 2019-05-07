"""
Input Format. The first line contains an integer 𝑛. The second line contains integers 𝑣1, 𝑣2, . . . , 𝑣𝑛 separated
by spaces.

Constraints. 1 ≤ 𝑛 ≤ 20, 1 ≤ 𝑣𝑖 ≤ 30 for all 𝑖.

Output Format. Output 1, if it possible to partition 𝑣1, 𝑣2, . . . , 𝑣𝑛 into three subsets with equal sums, and
0 otherwise.

"""


def partition3d(souvenirs):
    total = sum(souvenirs)
    souvenirs_len = len(souvenirs)

    if total % 3 != 0:
        return 0

    total = total//3
    v = init_matrix3d(total, total, souvenirs_len)

    for tot_1 in range(total+1):
        for tot_2 in range(total+1):
            for ai in range(souvenirs_len+1):
                if tot_1 == tot_2 == 0:
                    v[tot_1][tot_2][ai] = 1
                elif ai == 0 and (tot_1 != 0 or tot_2 != 0):
                    v[tot_1][tot_2][ai] = 0
                else:
                    a = souvenirs[ai - 1]
                    if tot_1 >= a:
                        d11 = v[tot_1-a][tot_2][ai-1]
                        d12 = v[tot_1][tot_2][ai - 1]
                        d1 = max(d11, d12)
                    else:
                        d1 = v[tot_1][tot_2][ai-1]
                    if tot_2 >= a:
                        d21 = v[tot_1][tot_2-a][ai-1]
                        d22 = v[tot_1][tot_2][ai-1]
                        d2 = max(d21, d22)
                    else:
                        d2 = v[tot_1][tot_2][ai-1]
                    v[tot_1][tot_2][ai] = max(d1, d2)

    return v[total][total][souvenirs_len]


def init_matrix(n1, n2):
    matrix = []
    for i in range(n1 + 1):
        row = []
        for j in range(n2 + 1):
            row.append(0)
        matrix.append(row)
    return matrix


def init_matrix3d(n1, n2, n3):
    matrix = []
    for i in range(n1+1):
        row = init_matrix(n2, n3)
        matrix.append(row)
    return matrix


if __name__ == '__main__':
    n, *A = list(map(int, input().split()))
    print(partition3d(A))

