"""
Task. The first step of the HeapSort algorithm is to create a heap from the array you want to sort. By the
way, did you know that algorithms based on Heaps are widely used for external sort, when you need
to sort huge files that don’t fit into memory of a computer?
Your task is to implement this first step and convert a given array of integers into a heap. You will
do that by applying a certain number of swaps to the array. Swap is an operation which exchanges
elements 𝑎𝑖 and 𝑎𝑗 of the array 𝑎 for some 𝑖 and 𝑗. You will need to convert the array into a heap
using only 𝑂(𝑛) swaps, as was described in the lectures. Note that you will need to use a min-heap
instead of a max-heap in this problem.

Input Format. The first line of the input contains single integer 𝑛. The next line contains 𝑛 space-separated
integers 𝑎𝑖.

Constraints. 1 ≤ 𝑛 ≤ 100 000; 0 ≤ 𝑖, 𝑗 ≤ 𝑛 − 1; 0 ≤ 𝑎0, 𝑎1, . . . , 𝑎𝑛−1 ≤ 109
. All 𝑎𝑖 are distinct.

Output Format. The first line of the output should contain single integer 𝑚 — the total number of swaps.
𝑚 must satisfy conditions 0 ≤ 𝑚 ≤ 4𝑛. The next 𝑚 lines should contain the swap operations used
to convert the array 𝑎 into a heap. Each swap is described by a pair of integers 𝑖, 𝑗 — the 0-based
indices of the elements to be swapped. After applying all the swaps in the specified order the array
must become a heap, that is, for each 𝑖 where 0 ≤ 𝑖 ≤ 𝑛 − 1 the following conditions must be true:
1. If 2𝑖 + 1 ≤ 𝑛 − 1, then 𝑎𝑖 < 𝑎2𝑖+1.
2. If 2𝑖 + 2 ≤ 𝑛 − 1, then 𝑎𝑖 < 𝑎2𝑖+2.
Note that all the elements of the input array are distinct. Note that any sequence of swaps that has
length at most 4𝑛 and after which your initial array becomes a correct heap will be graded as correct.
"""


class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = []
        self._size = None

    def read_data(self):
        n = int(input())
        self._size = n
        self._data = [int(s) for s in input().split()]
        assert n == len(self._data)

    def write_response(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def generate_swaps(self):
        n = len(self._data)
        for i in range((n-1)//2, -1, -1):
            self.shift_down(i)

    def shift_down(self, parent):
        min_index = parent

        left = parent*2+1

        if left < self._size and self._data[left] < self._data[min_index]:
            min_index = left

        right = parent*2+2

        if right < self._size and self._data[right] < self._data[min_index]:
            min_index = right

        if parent != min_index:
            self.swap(parent, min_index)
            self.shift_down(min_index)

    def swap(self, i, j):
        self._swaps.append((i, j))
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def solve(self):
        self.read_data()
        self.generate_swaps()
        self.write_response()


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.solve()
