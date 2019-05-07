"""
Task. The goal of this code problem is to implement an algorithm for the fractional knapsack problem.
Input Format. The first line of the input contains the number 𝑛 of items and the capacity 𝑊 of a knapsack.
The next 𝑛 lines define the values and weights of the items. The 𝑖-th line contains integers 𝑣𝑖 and 𝑤𝑖—the
value and the weight of 𝑖-th item, respectively.
Constraints. 1 ≤ 𝑛 ≤ 103, 0 ≤ 𝑊 ≤ 2 · 106; 0 ≤ 𝑣𝑖 ≤ 2 · 106, 0 < 𝑤𝑖 ≤ 2 · 106 for all 1 ≤ 𝑖 ≤ 𝑛.
All the numbers are integers.
Output Format. Output the maximal value of fractions of items that fit into the knapsack. The absolute
value of the difference between the answer of your program and the optimal value should be at most
10−3
. To ensure this, output your answer with at least four digits after the decimal point (otherwise
your answer, while being computed correctly, can turn out to be wrong because of rounding issues).

"""


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
    data = list(map(int, input().split()))
    n, c = data[0:2]
    v = data[2:(2 * n + 2):2]
    w = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(c, w, v)
    print("{:.10f}".format(opt_value))
