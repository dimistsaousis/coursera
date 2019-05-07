"""
Task. There are 𝑛 tables stored in some database. The tables are numbered from 1 to 𝑛. All tables share
the same set of columns. Each table contains either several rows with real data or a symbolic link to
another table. Initially, all tables contain data, and 𝑖-th table has 𝑟𝑖 rows. You need to perform 𝑚 of
the following operations:

1. Consider table number 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖.
Traverse the path of symbolic links to get to the data. That is, while 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 contains a symbolic link instead of
real data do 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 ← symlink(𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖)

2. Consider the table number 𝑠𝑜𝑢𝑟𝑐𝑒𝑖 and traverse the path of symbolic links from it in the same manner as for
𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛

3. Now, 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 and 𝑠𝑜𝑢𝑟𝑐𝑒𝑖 are the numbers of two tables with real data. If 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛!=𝑠𝑜𝑢𝑟𝑐𝑒, copy all the rows
from table 𝑠𝑜𝑢𝑟𝑐𝑒𝑖 to table 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 , then clear the table 𝑠𝑜𝑢𝑟𝑐𝑒𝑖 and instead of real data put a symbolic link to
𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 into it.

4. Print the maximum size among all 𝑛 tables (recall that size is the number of rows in the table).
If the table contains only a symbolic link, its size is considered to be 0.

Input Format. The first line of the input contains two integers 𝑛 and 𝑚 — the number of tables in the
database and the number of merge queries to perform, respectively.
The second line of the input contains 𝑛 integers 𝑟𝑖 — the number of rows in the 𝑖-th table.
Then follow 𝑚 lines describing merge queries. Each of them contains two integers 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 and
𝑠𝑜𝑢𝑟𝑐𝑒𝑖 — the numbers of the tables to merge.

Constraints. 1 ≤ 𝑛, 𝑚 ≤ 100 000; 0 ≤ 𝑟𝑖 ≤ 10 000; 1 ≤ 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 , 𝑠𝑜𝑢𝑟𝑐𝑒𝑖 ≤ 𝑛.

Output Format. For each query print a line containing a single integer — the maximum of the sizes of all
tables (in terms of the number of rows) after the corresponding operation.

Time Limits. C: 2 sec, C++: 2 sec, Java: 14 sec, Python: 6 sec. C#: 3 sec, Haskell: 4 sec, JavaScript: 6
sec, Ruby: 6 sec, Scala: 14 sec.
Memory Limit. 512Mb.
"""

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


def merge(d, s, res):
    real_destination, real_source = get_parent(d), get_parent(s)

    if real_destination == real_source:
        return res

    parent[real_source] = real_destination
    lines[real_destination] += lines[real_source]
    lines[real_source] = 0
    res = max(res, lines[real_destination])
    return res


for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    ans = merge(destination - 1, source - 1, ans)
    print(ans)
