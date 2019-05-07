# Uses python3
def evalt(a, b, op):
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
                v_value1 = evalt(v_min[i][i], v_min[i + 1][j], ops[i])
                v_value2 = evalt(v_min[i][i], v_max[i + 1][j], ops[i])
                v_value3 = evalt(v_max[i][i], v_min[i + 1][j], ops[i])
                v_value4 = evalt(v_max[i][i], v_max[i + 1][j], ops[i])
                t_min = min(v_value1, v_value2, v_value3, v_value4)
                t_max = max(v_value1, v_value2, v_value3, v_value4)
                for k in range(i+1, j):
                    v_value1 = evalt(v_min[i][k], v_min[k+1][j], ops[k])
                    v_value2 = evalt(v_min[i][k], v_max[k+1][j], ops[k])
                    v_value3 = evalt(v_max[i][k], v_min[k+1][j], ops[k])
                    v_value4 = evalt(v_max[i][k], v_max[k+1][j], ops[k])
                    t_min = min(v_value1, v_value2, v_value3, v_value4, t_min)
                    t_max = max(v_value1, v_value2, v_value3, v_value4, t_max)
                v_min[i][j] = t_min
                v_max[i][j] = t_max

    return v_max[0][n_digits-1]


def init_matrix(n, m):
    matrix = []
    for i in range(n):
        l = []
        for j in range(m):
            l.append(0)
        matrix.append(l)
    return matrix


if __name__ == "__main__":
    # A = '5-8+7*4-8+9'
    # print(get_maximum_value(A))
    print(get_maximum_value(input()))

