# python3

import sys


class Rope:
    def __init__(self, s):
        self.s = s

    def result(self):
        return self.s

    def process(self, i, j, k):
        cut = self.s[i:j+1]
        part1 = self.s[0:i]
        part2 = self.s[j+1:]
        new_s = part1 + part2
        self.s = new_s[0:k] + cut + new_s[k:]


if __name__ == '__main__':
    rope = Rope(sys.stdin.readline().strip())
    q = int(sys.stdin.readline())
    for _ in range(q):
        i, j, k = map(int, sys.stdin.readline().strip().split())
        rope.process(i, j, k)
    print(rope.result())
