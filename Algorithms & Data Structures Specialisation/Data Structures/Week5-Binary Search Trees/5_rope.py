"""
Task. You are given a string 𝑆 and you have to process 𝑛 queries. Each query is described by three integers
𝑖, 𝑗, 𝑘 and means to cut substring 𝑆[𝑖..𝑗] (𝑖 and 𝑗 are 0-based) from the string and then insert it after the
𝑘-th symbol of the remaining string (if the symbols are numbered from 1). If 𝑘 = 0, 𝑆[𝑖..𝑗] is inserted
in the beginning. See the examples for further clarification.

Input Format. The first line contains the initial string 𝑆.
The second line contains the number of queries 𝑞.
Next 𝑞 lines contain triples of integers 𝑖, 𝑗, 𝑘.

Constraints. 𝑆 contains only lowercase english letters. 1 ≤ |𝑆| ≤ 300 000; 1 ≤ 𝑞 ≤ 100 000; 0 ≤ 𝑖 ≤ 𝑗 ≤
𝑛 − 1; 0 ≤ 𝑘 ≤ 𝑛 − (𝑗 − 𝑖 + 1).

Output Format. Output the string after all 𝑞 queries.
"""

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
