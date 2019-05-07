# Uses python3
import sys


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
    # print(get_change(28))
    m = int(sys.stdin.read())
    print(get_change(m))
