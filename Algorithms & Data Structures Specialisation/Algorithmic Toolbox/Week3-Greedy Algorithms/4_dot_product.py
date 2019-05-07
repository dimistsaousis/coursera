"""
Task. Given two sequences 𝑎1, 𝑎2, . . . , 𝑎𝑛 (𝑎𝑖 is the profit per click of the 𝑖-th ad)
and 𝑏1, 𝑏2, . . . , 𝑏𝑛 (𝑏𝑖 is the average number of clicks per day of the 𝑖-th slot),
we need to partition them into 𝑛 pairs (𝑎𝑖 , 𝑏𝑗 ) such that the sum of their products is maximized.

Input Format. The first line contains an integer 𝑛, the second one contains a sequence of integers
𝑎1, 𝑎2, . . . , 𝑎𝑛, the third one contains a sequence of integers 𝑏1, 𝑏2, . . . , 𝑏𝑛.

Constraints. 1 ≤ 𝑛 ≤ 103; −105 ≤ 𝑎𝑖, 𝑏𝑖 ≤ 105 for all 1 ≤ 𝑖 ≤ 𝑛.

Output Format. Output the maximum value of ∑𝑎𝑖*𝑐𝑖, where 𝑐1, 𝑐2, . . . , 𝑐𝑛 is a permutation of 𝑏1, 𝑏2, . . . , 𝑏𝑛.
"""


def get_max_dot_product(a, b):
    a = sorted(a, reverse=True)
    b = sorted(b, reverse=True)
    res = 0

    for i in range(len(a)):
        res += a[i] * b[i]
    return res


if __name__ == '__main__':
    data = list(map(int, input().split()))
    n = data[0]
    a_ = data[1:(n + 1)]
    b_ = data[(n + 1):]
    print(get_max_dot_product(a_, b_))
