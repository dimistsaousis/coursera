"""
Task. In this task your goal is to implement a simple phone book manager. It should be able to process
the following types of user’s queries:

∙ add number name. It means that the user adds a person with name name and phone number number to the phone book.
If there exists a user with such number already, then your manager has to overwrite the corresponding name.

∙ del number. It means that the manager should erase a person with number number from the phone book.
If there is no such person, then it should just ignore the query.

∙ find number. It means that the user looks for a person with phone number number. The manager should reply
with the appropriate name, or with string “not found" (without quotes) if there is no such person in the book.

Input Format. There is a single integer 𝑁 in the first line — the number of queries. It’s followed by 𝑁
lines, each of them contains one query in the format described above.

Constraints. 1 ≤ 𝑁 ≤ 105

. All phone numbers consist of decimal digits, they don’t have leading zeros,
and each of them has no more than 7 digits. All names are non-empty strings of latin letters, and each
of them has length at most 15. It’s guaranteed that there is no person with name “not found".

Output Format. Print the result of each find query — the name corresponding to the phone number or
“not found" (without quotes) if there is no person in the phone book with such phone number. Output
one result per line in the same order as the find queries are given in the input.

Time Limits. C: 3 sec, C++: 3 sec, Java: 6 sec, Python: 6 sec. C#: 4.5 sec, Haskell: 6 sec, JavaScript:
9 sec, Ruby: 9 sec, Scala: 9 sec.
"""


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries():
    n = int(input())
    return [Query(input().split()) for _ in range(n)]


def write_responses(result):
    print('\n'.join(result))


def process_queries(queries):
    phone_book = {}
    result = []
    for cur_query in queries:
        if cur_query.type == 'add':
            phone_book[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            phone_book.pop(cur_query.number, False)
        else:
            if cur_query.number in phone_book:
                result.append(phone_book[cur_query.number])
            else:
                result.append("not found")
    return result


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

