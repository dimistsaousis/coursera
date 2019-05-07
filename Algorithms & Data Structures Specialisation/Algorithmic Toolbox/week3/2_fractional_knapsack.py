# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    n = len(weights)
    dic = dict()
    for i in range(n):
        dic[i] = values[i]/weights[i]
    dic_invert = {v: k for k, v in dic.items()}

    value_over_weight_sorted = sorted(dic.values(), reverse=True)

    total_value = 0
    for v in value_over_weight_sorted:
        weight = weights[dic_invert[v]]
        value = values[dic_invert[v]]

        if capacity > 0:
            fraction = min(capacity/weight, 1)
            capacity -= fraction*weight
            total_value += value*fraction
        else:
            return total_value

    return total_value


if __name__ == "__main__":
    # capacity = 10
    # values = [500]
    # weights = [30]
    # print(get_optimal_value(capacity, weights, values))
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
