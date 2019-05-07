# python3


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


def rabin_karp(p, t):
    result = []
    prime = 1000000007
    multiplier = 263
    size_pattern = len(p)
    size_text = len(t)
    p_hash = poly_hash(p, prime, multiplier)

    h = compute_hashes(t, size_pattern, prime, multiplier)

    for i in range(size_text-size_pattern+1):
        if p_hash == h[i] and t[i:i+size_pattern] == p:
            result.append(i)

    return result


if __name__ == '__main__':
    p = input().rstrip()
    t = input().rstrip()
    result = rabin_karp(p, t)
    print(' '.join(map(str, result)))

