# python3

import sys
n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)


def get_parent(table):
    all_tables = []
    while table != parent[table]:
        all_tables.append(table)
        table = parent[table]

    for t in all_tables:
        parent[t] = table
    return parent[table]


def merge(d, s, ans):
    real_destination, real_source = get_parent(d), get_parent(s)

    if real_destination == real_source:
        return ans

    parent[real_source] = real_destination
    lines[real_destination] += lines[real_source]
    lines[real_source] = 0
    ans = max(ans, lines[real_destination])
    return ans


for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    ans = merge(destination - 1, source - 1, ans)
    print(ans)


# if __name__ == '__main__':
#     n, m = map(int, sys.stdin.readline().split())
#     lines = list(map(int, sys.stdin.readline().split()))
#     rank = [1] * n
#     parent = list(range(0, n))
#     ans = max(lines)
#
#     for i in range(m):
#         destination, source = map(int, sys.stdin.readline().split())
#         merge(destination - 1, source - 1)
#         print(max(lines))
