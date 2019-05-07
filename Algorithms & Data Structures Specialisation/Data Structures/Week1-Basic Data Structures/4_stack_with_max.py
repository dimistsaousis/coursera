"""
Task. Implement a stack supporting the operations Push(), Pop(), and Max().
Input Format. The first line of the input contains the number 𝑞 of queries. Each of the following 𝑞 lines
specifies a query of one of the following formats: push v, pop, or max.
Constraints. 1 ≤ 𝑞 ≤ 400 000, 0 ≤ 𝑣 ≤ 10 000.
Output Format. For each max query, output (on a separate line) the maximum value of the stack.
"""
import sys


class StackWithMax:
    def __init__(self):
        self.__stack = []
        self.__max = []

    def push(self, a):
        new_max = max(self.__max[-1], a) if self.__max else a
        self.__max.append(new_max)
        self.__stack.append(a)

    def pop(self):
        assert(len(self.__stack))
        self.__max.pop()
        self.__stack.pop()

    def max(self):
        return self.__max[-1]


if __name__ == '__main__':
    stack = StackWithMax()
    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.push(int(query[1]))
        elif query[0] == "pop":
            stack.pop()
        elif query[0] == "max":
            print(stack.max())
        else:
            assert False
