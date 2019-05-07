# python3


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
