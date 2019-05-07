"""
Task. Compose the largest number out of a set of integers.

Input Format. The first line of the input contains an integer 𝑛. The second line contains integers 𝑎1, 𝑎2, . . . , 𝑎𝑛.

Constraints. 1 ≤ 𝑛 ≤ 100; 1 ≤ 𝑎𝑖 ≤ 103 for all 1 ≤ 𝑖 ≤ 𝑛.

Output Format. Output the largest number that can be composed out of 𝑎1, 𝑎2, . . . , 𝑎𝑛.
"""


def get_optimal_summands(n):
    summands = []
    price = 1
    while n > 0:
        if 2*price+1 > n:
            summands.append(n)
            n = 0
        else:
            n -= price
            summands.append(price)
            price += 1

    return summands


if __name__ == '__main__':
    n = int(input())
    res = get_optimal_summands(n)
    print(len(res))
    for x in res:
        print(x, end=' ')
