# python3
import sys
from collections import defaultdict


def count_sort(string, alphabet):
    alphabet_to_idx = {a: i for i, a in enumerate(alphabet)}
    char_sorted_count = [0]*len(alphabet)
    char_count_before_i = defaultdict(lambda: [0]*(len(string)+1))
    for i, el in enumerate(string):
        idx = alphabet_to_idx[el]
        char_sorted_count[idx] += 1
        char_count_before_i[el][i+1] = char_sorted_count[idx]
        for k in char_count_before_i.keys():
            if k != el:
                char_count_before_i[k][i+1] = char_count_before_i[k][i]
    return char_sorted_count, char_count_before_i


def preprocessed_bwt(b):
    alphabet = '$ACGT'
    char_sorted_count, char_count_before = count_sort(b, alphabet)
    first_occurrence = dict()
    c_total = 0
    for i, c in enumerate(char_sorted_count):
        if c > 0:
            char = alphabet[i]
            first_occurrence[char] = c_total
            c_total += c
    return first_occurrence, char_count_before


def count_occurrences(p, last_column, first_occurrence, char_count_before):
    top = 0
    bottom = len(last_column)-1
    while top <= bottom:
        if len(p) > 0:
            symbol = p[-1]
            p = p[:-1]
            if char_count_before[symbol][bottom+1] - (char_count_before[symbol][top] if top > 0 else 0) > 0:
                top = first_occurrence[symbol] + char_count_before[symbol][top]
                bottom = first_occurrence[symbol] + char_count_before[symbol][bottom+1]-1
            else:
                return 0
        else:
            return bottom-top+1


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    starts, occ_counts_before = preprocessed_bwt(bwt)
    occurrence_counts = []
    for pattern in patterns:
        occurrence_counts.append(count_occurrences(pattern, bwt, starts, occ_counts_before))
    print(' '.join(map(str, occurrence_counts)))
