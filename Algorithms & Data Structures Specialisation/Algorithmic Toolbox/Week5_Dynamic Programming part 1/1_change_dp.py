"""
Input Format. Integer money.
Output Format. The minimum number of coins with denominations 1, 3, 4 that changes money.
Constraints. 1 ≤ money ≤ 103.
"""


def get_change(money):
    d = {1: 1,
         2: 2,
         3: 1,
         4: 1}

    for i in range(5, money + 1):
        d1 = d[i-1]+1
        d2 = d[i-3]+1
        d3 = d[i-4]+1
        d[i] = min(d1, d2, d3)

    return d[money]


if __name__ == '__main__':
    print(get_change(int(input())))
