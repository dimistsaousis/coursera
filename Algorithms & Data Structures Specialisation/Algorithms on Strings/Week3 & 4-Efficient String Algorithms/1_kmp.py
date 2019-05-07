"""
Task. Find all occurrences of a pattern in a string.
Input Format. Strings 𝑃 𝑎𝑡𝑡𝑒𝑟𝑛 and 𝐺𝑒𝑛𝑜𝑚𝑒.

Constraints. 1 ≤ |𝑃 𝑎𝑡𝑡𝑒𝑟𝑛| ≤ 106 ; 1 ≤ |𝐺𝑒𝑛𝑜𝑚𝑒| ≤ 106 ; both strings are over A, C, G, T.

Output Format. All starting positions in 𝐺𝑒𝑛𝑜𝑚𝑒 where 𝑃 𝑎𝑡𝑡𝑒𝑟𝑛 appears as a substring (using 0-based indexing as usual).
"""


def find_pattern(pattern, text):
    len_p = len(pattern)
    len_t = len(text)
    s = pattern + "$" + text
    s = compute_prefix_function(s)
    result = []

    for i in range(len_p+1, len_p+len_t+1):
        if s[i] == len_p:
            result.append(i-2*len_p)

    return result


def compute_prefix_function(text):
    len_t = len(text)
    s = [0]*len_t
    s[0] = 0
    border = 0

    for i in range(1, len_t):
        while border > 0 and text[i] != text[border]:
            border = s[border-1]
        if text[i] == text[border]:
            border += 1
        else:
            border = 0
        s[i] = border

    return s


if __name__ == '__main__':
    p = input().strip()
    t = input().strip()
    res = find_pattern(p, t)
    print(" ".join(map(str, res)))

