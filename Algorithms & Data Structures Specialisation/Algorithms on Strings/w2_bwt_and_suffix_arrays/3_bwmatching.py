"""
Task. Implement BetterBWMatching algorithm.
Input Format. A string BWT(Text), followed by an integer 𝑛 and a collection of 𝑛 strings Patterns =
{𝑝1, . . . , 𝑝𝑛} (on one line separated by spaces).

Constraints. 1 ≤ |BWT(Text)| ≤ 106; except for the one $ symbol, BWT(Text) contains symbols A, C, G, T only;
1 ≤ 𝑛 ≤ 5 000; for all 1 ≤ 𝑖 ≤ 𝑛, 𝑝𝑖 is a string over A, C, G, T; 1 ≤ |𝑝𝑖 | ≤ 1 000.

Output Format. A list of integers, where the 𝑖-th integer corresponds to the number of substring matches
of the 𝑖-th member of Patterns in Text.
"""
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
    bwt = input().strip()
    pattern_count = int(input().strip())
    patterns = input().strip().split()
    starts, occ_counts_before = preprocessed_bwt(bwt)
    occurrence_counts = []
    for pattern in patterns:
        occurrence_counts.append(count_occurrences(pattern, bwt, starts, occ_counts_before))
    print(' '.join(map(str, occurrence_counts)))
