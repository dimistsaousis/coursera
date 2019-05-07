#python3
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
    # stack = StackWithMax()
    # queries = ['push 7', 'push 1', 'push 7', 'max', 'pop', 'max']
    # for q in queries:
    #     query = q.split()
    #     if query[0] == "push":
    #         stack.push(int(query[1]))
    #     elif query[0] == "pop":
    #         stack.pop()
    #     elif query[0] == "max":
    #         print(stack.max())
    #     else:
    #         assert False
    #
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
