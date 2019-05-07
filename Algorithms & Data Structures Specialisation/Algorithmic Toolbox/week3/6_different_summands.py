# Uses python3
import sys


def optimal_summands(n):
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
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
