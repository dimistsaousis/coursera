"""
Task. The goal in this problem is to count the number of inversions of a given sequence.

Input Format. The first line contains an integer 𝑛, the next one contains a sequence of integers 𝑎0, 𝑎1, . . . , 𝑎𝑛−1.

Constraints. 1 ≤ 𝑛 ≤ 105, 1 ≤ 𝑎𝑖 ≤ 109 for all 0 ≤ 𝑖 < 𝑛.

Output Format. Output the number of inversions in the sequence.
"""


def merge_sort(array, left, right, inversions=0):
    if left == right:
        return array[left], inversions

    m = (left+right)//2

    b, inversions = merge_sort(array, left, m, inversions)
    c, inversions = merge_sort(array, m + 1, right, inversions)
    return merge(b, c, inversions)


def merge(arr_1, arr_2, inversions):
    res = []
    arr_1 = arr_1 if isinstance(arr_1, list) else [arr_1]
    arr_2 = arr_2 if isinstance(arr_2, list) else [arr_2]
    while arr_1 and arr_2:
        if arr_1[0] <= arr_2[0]:
            res.append(arr_1[0])
            arr_1.pop(0)
        else:
            res.append(arr_2[0])
            arr_2.pop(0)
            inversions += len(arr_1)
    if arr_1:
        res += arr_1
    if arr_2:
        res += arr_2
    return res, inversions


def naive_sort(array):
    arr_size = len(array)
    inversions = 0
    for i in range(arr_size):
        for j in range(i, arr_size):
            if array[i] > array[j]:
                inversions += 1
    return inversions


def sanity_check():
    import random
    while True:
        size_arr = random.randint(2, 5)
        array = []
        for _ in range(size_arr):
            array.append(random.randint(0, 10))

        if naive_sort(array) != merge_sort(array, 0, len(array) - 1)[1]:
            print(array)
            print("WRONG")
            break


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *arr = list(map(int, input.split()))
    print(merge_sort(arr, 0, len(arr) - 1)[1])
