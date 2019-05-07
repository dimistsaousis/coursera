"""
Task. In this problem your goal is to implement the Rabin–Karp’s algorithm for searching the given pattern
in the given text.

Input Format. There are two strings in the input: the pattern 𝑃 and the text 𝑇.

Constraints. 1 ≤ |𝑃| ≤ |𝑇| ≤ 5 · 105
. The total length of all occurrences of 𝑃 in 𝑇 doesn’t exceed 108
. The pattern and the text contain only latin letters.

Output Format. Print all the positions of the occurrences of 𝑃 in 𝑇 in the ascending order. Use 0-based
indexing of positions in the the text 𝑇.

Time Limits. C: 1 sec, C++: 1 sec, Java: 5 sec, Python: 5 sec. C#: 1.5 sec, Haskell: 2 sec, JavaScript:
3 sec, Ruby: 3 sec, Scala: 3 sec.

Memory Limit. 512Mb
"""


def read_input():
    return input().rstrip(), input().rstrip()


def compute_hashes(text, size_pattern, p, x):
    size_text = len(text)

    h = [None for _ in range(size_text-size_pattern+1)]

    s = text[size_text-size_pattern:size_text]
    h[size_text-size_pattern] = poly_hash(s, p, x)

    y = 1
    for i in range(size_pattern):
        y = y*x % p
    for i in range(size_text-size_pattern-1, -1, -1):
        h[i] = (x*h[i+1]+ord(text[i])-y*ord(text[i+size_pattern])) % p
    return h


def poly_hash(s, p, x):
        ans = 0
        for c in reversed(s):
            ans = (ans * x + ord(c)) % p
        return ans


def rabin_karp(pattern, text):
    res = []
    prime = 1000000007
    multiplier = 263
    size_pattern = len(pattern)
    size_text = len(text)
    p_hash = poly_hash(pattern, prime, multiplier)

    h = compute_hashes(text, size_pattern, prime, multiplier)

    for i in range(size_text-size_pattern+1):
        if p_hash == h[i] and text[i:i + size_pattern] == pattern:
            res.append(i)

    return res


if __name__ == '__main__':
    p = input().rstrip()
    t = input().rstrip()
    result = rabin_karp(p, t)
    print(' '.join(map(str, result)))

