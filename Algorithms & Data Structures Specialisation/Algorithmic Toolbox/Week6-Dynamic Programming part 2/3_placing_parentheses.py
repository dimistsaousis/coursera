"""
Task. Find the maximum value of an arithmetic expression by specifying the order of applying its arithmetic
operations using additional parentheses.

Input Format. The only line of the input contains a string 𝑠 of length 2𝑛 + 1 for some 𝑛, with symbols
𝑠0, 𝑠1, . . . , 𝑠2𝑛. Each symbol at an even position of 𝑠 is a digit (that is, an integer from 0 to 9) while
each symbol at an odd position is one of three operations from {+,-,*}.

Constraints. 1 ≤ 𝑛 ≤ 14 (hence the string contains at most 29 symbols).

Output Format. Output the maximum possible value of the given arithmetic expression among different
orders of applying arithmetic operations
"""


# Uses python3
def eval_func(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def get_maximum_value(dataset):
    n_dataset = len(dataset)

    digits = [int(dataset[i]) for i in range(0, n_dataset, 2)]
    ops = [dataset[i] for i in range(1, n_dataset, 2)]

    n_digits = len(digits)

    v_min = init_matrix(n_digits, n_digits)
    v_max = init_matrix(n_digits, n_digits)

    for s in range(n_digits):
        for i in range(n_digits-s):
            j = i+s
            if s == 0:
                v_min[i][j] = digits[i]
                v_max[i][j] = digits[i]
            else:
                v_value1 = eval_func(v_min[i][i], v_min[i + 1][j], ops[i])
                v_value2 = eval_func(v_min[i][i], v_max[i + 1][j], ops[i])
                v_value3 = eval_func(v_max[i][i], v_min[i + 1][j], ops[i])
                v_value4 = eval_func(v_max[i][i], v_max[i + 1][j], ops[i])
                t_min = min(v_value1, v_value2, v_value3, v_value4)
                t_max = max(v_value1, v_value2, v_value3, v_value4)
                for k in range(i+1, j):
                    v_value1 = eval_func(v_min[i][k], v_min[k + 1][j], ops[k])
                    v_value2 = eval_func(v_min[i][k], v_max[k + 1][j], ops[k])
                    v_value3 = eval_func(v_max[i][k], v_min[k + 1][j], ops[k])
                    v_value4 = eval_func(v_max[i][k], v_max[k + 1][j], ops[k])
                    t_min = min(v_value1, v_value2, v_value3, v_value4, t_min)
                    t_max = max(v_value1, v_value2, v_value3, v_value4, t_max)
                v_min[i][j] = t_min
                v_max[i][j] = t_max

    return v_max[0][n_digits-1]


def init_matrix(n, m):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(0)
        matrix.append(row)
    return matrix


if __name__ == "__main__":
    print(get_maximum_value(input()))

