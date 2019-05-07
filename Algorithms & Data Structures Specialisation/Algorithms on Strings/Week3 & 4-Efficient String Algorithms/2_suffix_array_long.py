"""
Task. Construct the suffix array of a string.

Input Format. A string Text ending with a “$” symbol. Constraints. 1 ≤ |Text(Text)| ≤ 2 · 105; except for the last
symbol, Text contains symbols A, C, G, T only.

Output Format. SuffixArray(Text), that is, the list of starting positions of sorted suffixes separated by spaces.
"""


def build_suffix_array(text):
    abc = '$ACGT'
    abc_dic = {a: i for i, a in enumerate(abc)}
    len_text = len(text)

    text_order = sort_characters(text, abc, abc_dic)
    text_class = compute_char_classes(text, text_order)

    layer = 1
    while layer <= len_text:
        text_order = sort_doubled(text, layer, text_order, text_class)
        text_class = update_classes(text_order, text_class, layer)
        layer = 2*layer

    return text_order


def sort_characters(text, abc, abc_dic):
    len_text = len(text)
    len_abc = len(abc)
    char_order = [0]*len_text
    char_count = [0]*len_abc

    for i, c in enumerate(text):
        idx = abc_dic[c]
        char_count[idx] += 1

    for j in range(1, len_abc):
        char_count[j] += char_count[j-1]

    for i in range(len_text-1, -1, -1):
        c = text[i]
        idx = abc_dic[c]
        char_count[idx] = char_count[idx]-1
        char_order[char_count[idx]] = i

    return char_order


def compute_char_classes(text, text_order):
    len_text = len(text)
    char_class = [0]*len_text
    char_class[text_order[0]] = 0

    for i in range(1, len_text):
        if text[text_order[i-1]] != text[text_order[i]]:
            char_class[text_order[i]] = char_class[text_order[i-1]] + 1
        else:
            char_class[text_order[i]] = char_class[text_order[i - 1]]

    return char_class


def sort_doubled(text, layer, text_order, text_class):
    len_text = len(text)

    count = [0]*len_text
    new_order = [0]*len_text

    for i in range(len_text):
        count[text_class[i]] = count[text_class[i]]+1
    for j in range(1, len_text):
        count[j] += count[j-1]
    for i in range(len_text-1, -1, -1):
        start = (text_order[i] - layer + len_text) % len_text
        cl = text_class[start]
        count[cl] = count[cl]-1
        new_order[count[cl]] = start

    return new_order


def update_classes(text_order, text_class, layer):
    n = len(text_order)
    new_class = [0]*n
    new_class[text_order[0]] = 0

    for i in range(1, n):
        cur = text_order[i]
        prev = text_order[i-1]
        mid = (cur+layer) % n
        mid_prev = (prev+layer) % n
        if text_class[cur] != text_class[prev] or text_class[mid] != text_class[mid_prev]:
            new_class[cur] = new_class[prev] + 1
        else:
            new_class[cur] = new_class[prev]
    return new_class


if __name__ == '__main__':
    t = input().strip()
    print(" ".join(map(str, build_suffix_array(t))))
