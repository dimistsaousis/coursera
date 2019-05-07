# python3


class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, m):
        self.m = m
        # store all strings in one list
        self.hash = [list() for _ in range(m)]

    def add(self, s):
        pos = self._hash_func(s)
        if s not in self.hash[pos]:
            self.hash[pos] = [s] + self.hash[pos]

    def find(self, s):
        pos = self._hash_func(s)
        return s in self.hash[pos]

    def delete(self, s):
        pos = self._hash_func(s)
        if s in self.hash[pos]:
            for i, hash_s in enumerate(self.hash[pos]):
                if hash_s == s:
                    self.hash[pos].pop(i)

    def check(self, i):
        return self.hash[i]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.m

    @staticmethod
    def write_search_result(was_found):
        print('yes' if was_found else 'no')

    @staticmethod
    def write_chain(chain):
        print(' '.join(chain))

    @staticmethod
    def read_query():
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            self.write_chain(self.check(query.ind))
        else:
            if query.type == 'find':
                self.write_search_result(self.find(query.s))
            elif query.type == 'add':
                self.add(query.s)
            else:
                self.delete(query.s)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())


if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
