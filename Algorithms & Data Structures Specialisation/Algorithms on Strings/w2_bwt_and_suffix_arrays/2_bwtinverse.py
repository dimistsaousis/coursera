"""
Task. Reconstruct a string from its Burrows–Wheeler transform.

Input Format. A string Transform with a single “$” sign.

Constraints. 1 ≤ |Transform| ≤ 1 000 000; except for the last symbol, Text contains symbols A, C, G, T
only.

Output Format. The string Text such that BWT(Text) = Transform. (There exists a unique such string.)
"""


def get_inverse_bwt(bwt):
    count = [0, 0, 0, 0, 0]
    bwt_tup = []
    for i, el in enumerate(bwt):
        if el == '$':
            count[0] += 1
            bwt_tup.append((el, count[0]))
        elif el == 'A':
            count[1] += 1
            bwt_tup.append((el, count[1]))
        elif el == 'C':
            count[2] += 1
            bwt_tup.append((el, count[2]))
        elif el == 'G':
            count[3] += 1
            bwt_tup.append((el, count[3]))
        elif el == 'T':
            count[4] += 1
            bwt_tup.append((el, count[4]))

    alphabet = '$ACGT'
    first_tup = []
    first_idx = {}
    for i, c in enumerate(count):
        for j in range(c):
            first_tup.append((alphabet[i], j+1))
            first_idx[(alphabet[i], j+1)] = len(first_tup)-1

    t = []
    row = 0
    el = first_tup[row][0]
    t.append(el)
    row = first_idx[bwt_tup[row]]
    el = first_tup[row][0]
    while el != '$':
        t.append(el)
        row = first_idx[bwt_tup[row]]
        el = first_tup[row][0]

    return "".join(reversed(t))


if __name__ == '__main__':
    bwt_ = input().strip()
    print(get_inverse_bwt(bwt_))
