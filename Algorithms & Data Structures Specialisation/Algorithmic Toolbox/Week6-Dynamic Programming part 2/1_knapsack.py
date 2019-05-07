"""
Task. Given 𝑛 gold bars, find the maximum weight of gold that fits into a bag of capacity 𝑊.

Input Format. The first line of the input contains the capacity 𝑊 of a knapsack and the number 𝑛 of bars
of gold. The next line contains 𝑛 integers 𝑤0, 𝑤1, . . . , 𝑤𝑛−1 defining the weights of the bars of gold.

Constraints. 1 ≤ 𝑊 ≤ 104 ; 1 ≤ 𝑛 ≤ 300; 0 ≤ 𝑤0, . . . , 𝑤𝑛−1 ≤ 105.

Output Format. Output the maximum weight of gold that fits into a knapsack of capacity 𝑊.

"""


def init_matrix(rows, cols):
    matrix = []
    for i in range(rows + 1):
        row = []
        for j in range(cols + 1):
            row.append(0)
        matrix.append(row)
    return matrix


def optimal_weight(capacity, weights):
    wn = len(weights)
    v = init_matrix(capacity, wn)
    for i in range(capacity + 1):
        for j in range(wn+1):
            if i != 0 and j != 0:
                if weights[j - 1] > i:
                    v[i][j] = v[i][j-1]
                else:
                    d1 = v[i - weights[j - 1]][j - 1] + weights[j - 1]
                    d2 = v[i][j - 1]
                    v[i][j] = max(d1, d2)
    return v[capacity][wn]


if __name__ == '__main__':
    total, n, *w = list(map(int, input().split()))
    print(optimal_weight(total, w))
