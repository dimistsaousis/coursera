# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i))

        elif next in ")]}":
            if opening_brackets_stack:
                previous = opening_brackets_stack.pop().char
                if next == ')' and previous != '(':
                    return i+1
                if next == ']' and previous != '[':
                    return i+1
                if next == '}' and previous != '{':
                    return i+1
            else:
                return i+1

    if opening_brackets_stack:
        return opening_brackets_stack.pop().position+1
    else:
        return 'Success'


def main():
    # text = 'foo(bar[i);'
    # print(find_mismatch(text))
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
