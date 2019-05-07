# Uses python3
import sys


def optimal_sequence(n):
    d = {1: [1], 2: [1, 2], 3: [1, 3]}

    for i in range(4, n+1):
        s = d[i-1]

        if i % 3 == 0:
            s_ = d[i//3]
            if len(s_) < len(s):
                s = s_

        if i % 2 == 0:
            s_ = d[i//2]
            if len(s_) < len(s):
                s = s_

        s = s+[i]
        d[i] = s

    return d[n]


# if __name__ == '__main__':
#     print(optimal_sequence(96234))


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
