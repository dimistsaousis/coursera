"""
Task. To force the given implementation of the quick sort algorithm to efficiently process sequences with
few unique elements, your goal is replace a 2-way partition with a 3-way partition. That is, your new
partition procedure should partition the array into three parts: < 𝑥 part, = 𝑥 part, and > 𝑥 part.

Input Format. The first line of the input contains an integer 𝑛. The next line contains a sequence of 𝑛
integers 𝑎0, 𝑎1, . . . , 𝑎𝑛−1.

Constraints. 1 ≤ 𝑛 ≤ 105 ; 1 ≤ 𝑎𝑖 ≤ 109 for all 0 ≤ 𝑖 < 𝑛.

Output Format. Output this sequence sorted in non-decreasing order.
"""


def partition(array, low, high):
    el_low = array[low]
    idx_1 = low

    # Strictly smaller
    for i in range(low+1, high+1):
        if array[i] < el_low:
            idx_1 += 1
            array[i], array[idx_1] = array[idx_1], array[i]
    array[low], array[idx_1] = array[idx_1], array[low]

    idx_2 = idx_1

    for i in range(idx_1+1, high+1):
        if array[i] == el_low:
            idx_2 += 1
            array[i], array[idx_2] = array[idx_2], array[i]

    return idx_1, idx_2


def randomized_quick_sort(array, low, high):
    import random
    if low >= high:
        return array
    k = random.randint(low, high)
    array[low], array[k] = array[k], array[low]
    idx_1, idx_2 = partition(array, low, high)
    randomized_quick_sort(array, low, idx_1 - 1)
    randomized_quick_sort(array, idx_2 + 1, high)


if __name__ == '__main__':
    n, *arr = list(map(int, input().split()))
    randomized_quick_sort(arr, 0, n - 1)
    for element in arr:
        print(element, end=' ')
