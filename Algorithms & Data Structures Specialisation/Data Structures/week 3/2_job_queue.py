# python3


class JobQueue:
    def __init__(self):
        self._num_workers, m = map(int, input().split())
        self.workers_heap = Heap([[i, 0] for i in range(self._num_workers)], self._num_workers)

        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)
        self.assigned_workers = []
        self.start_times = []

    def write_response(self):
        for i in range(len(self.jobs)):
            print(self.assigned_workers[i], self.start_times[i])

    def assign_jobs(self):
        for i, j in enumerate(self.jobs):
            thread, start_time = self.workers_heap.extract_max(j)
            self.assigned_workers.append(thread)
            self.start_times.append(start_time)

    def solve(self):
        self.assign_jobs()
        self.write_response()


class Heap:
    def __init__(self, workers, size):
        self._workers = workers
        self._size = size

    def extract_max(self, job_time):
        thread = self._workers[0][0]
        start_time = self._workers[0][1]
        self._workers[0][1] += job_time
        self.shift_down(0)
        return thread, start_time

    def swap(self, i, j):
        self._workers[i], self._workers[j] = self._workers[j], self._workers[i]

    def shift_down(self, i):
        min_index = i

        left = i*2+1

        if left < self._size and self.less_than(left, min_index):
            min_index = left

        right = i*2+2
        if right < self._size and self.less_than(right, min_index):
            min_index = right

        if min_index != i:
            self.swap(i, min_index)
            self.shift_down(min_index)

    def less_than(self, i, j):
        if self._workers[i][1] < self._workers[j][1]:
            return True
        if self._workers[i][1] > self._workers[j][1]:
            return False
        return self._workers[i][0] < self._workers[j][0]


if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

