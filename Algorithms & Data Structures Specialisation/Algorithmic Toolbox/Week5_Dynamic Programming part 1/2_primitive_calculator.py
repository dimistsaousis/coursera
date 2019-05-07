"""
Task. Given an integer 𝑛, compute the minimum number of operations needed to obtain the number 𝑛
starting from the number 1.

Input Format. The input consists of a single integer 1 ≤ 𝑛 ≤ 106.

Output Format. In the first line, output the minimum number 𝑘 of operations needed to get 𝑛 from 1.
In the second line output a sequence of intermediate numbers. That is, the second line should contain
positive integers 𝑎0, 𝑎2, . . . , 𝑎𝑘−1 such that 𝑎0 = 1, 𝑎𝑘−1 = 𝑛 and for all 0 ≤ 𝑖 < 𝑘 − 1, �
"""


def get_optimal_sequence(n):
    d = {1: [1], 2: [1, 2], 3: [1, 3]}

    for i in range(4, n+1):
        s = d[i-1]

        if i % 3 == 0:
            s_ = d[i//3]
            if len(s_) < len(s):
                s = s_

        if i % 2 == 0:
            s_ = d[i//2]
            if len(s_) < len(s):
                s = s_

        s = s+[i]
        d[i] = s

    return d[n]


if __name__ == '__main__':
    n_input = int(input())
    sequence = list(get_optimal_sequence(n_input))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
