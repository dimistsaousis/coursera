"""
Task. The goal in this code problem is to implement the binary search algorithm.

Input Format.
The first line of the input contains an integer 𝑛 and a sequence 𝑎0 < 𝑎1 < . . . < 𝑎𝑛−1 of 𝑛 pairwise distinct positive
integers in increasing order.
The next line contains an integer 𝑘 and 𝑘 positive integers 𝑏0, 𝑏1, . . . , 𝑏𝑘−1.

Constraints. 1 ≤ 𝑛, 𝑘 ≤ 104; 1 ≤ 𝑎𝑖 ≤ 109 for all 0 ≤ 𝑖 < 𝑛; 1 ≤ 𝑏𝑗 ≤ 109 for all 0 ≤ 𝑗 < 𝑘;

Output Format. For all 𝑖 from 0 to 𝑘 − 1, output an index 0 ≤ 𝑗 ≤ 𝑛 − 1 such that 𝑎𝑗 = 𝑏𝑖 or −1 if there
is no such index.
"""


def binary_search(array, lookup_value, low=0, high=None):
    high = len(array) if high is None else high

    while low <= high:
        mid = (high+low)//2

        if array[mid] == lookup_value:
            return mid

        elif array[mid] < lookup_value:
            low = mid+1

        else:
            high = mid-1

    return -1


if __name__ == '__main__':
    data = list(map(int, input().split()))
    n = data[0]
    m = data[n + 1]
    a = data[1:n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x, 0, n-1), end=' ')
