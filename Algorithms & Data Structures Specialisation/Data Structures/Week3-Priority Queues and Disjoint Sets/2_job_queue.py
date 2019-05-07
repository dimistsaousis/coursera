"""
Task. You have a program which is parallelized and uses 𝑛 independent threads to process the given list
of 𝑚 jobs. Threads take jobs in the order they are given in the input. If there is a free thread,
it immediately takes the next job from the list. If a thread has started processing a job, it doesn’t
interrupt or stop until it finishes processing the job. If several threads try to take jobs from the list
simultaneously, the thread with smaller index takes the job. For each job you know exactly how long
will it take any thread to process this job, and this time is the same for all the threads. You need to
determine for each job which thread will process it and when will it start processing.

Input Format. The first line of the input contains integers 𝑛 and 𝑚.
The second line contains 𝑚 integers 𝑡𝑖 — the times in seconds it takes any thread to process 𝑖-th job.
The times are given in the same order as they are in the list from which threads take jobs.
Threads are indexed starting from 0.

Constraints. 1 ≤ 𝑛 ≤ 105 ; 1 ≤ 𝑚 ≤ 105 ; 0 ≤ 𝑡𝑖 ≤ 109.

Output Format. Output exactly 𝑚 lines. 𝑖-th line (0-based index is used) should contain two spaceseparated integers —
the 0-based index of the thread which will process the 𝑖-th job and the time in
seconds when it will start processing that job.
"""


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

