"""
Task. The goal in this problem is to find the minimum number of coins needed to change the input value
(an integer) into coins with denominations 1, 5, and 10.
Input Format. The input consists of a single integer 𝑚.
Constraints. 1 ≤ 𝑚 ≤ 103.
Output Format. Output the minimum number of coins with denominations 1, 5, 10 that changes 𝑚.
"""


def get_change(m):
    denominations = [10, 5, 1]
    change_left = m
    number_of_coins = 0

    for change in denominations:
        if change_left >= change:
            number_of_change = change_left//change
            number_of_coins += number_of_change
            change_left -= number_of_change*change
        if change_left == 0:
            return number_of_coins
    return number_of_coins


if __name__ == '__main__':
    m_ = int(input())
    print(get_change(m_))
