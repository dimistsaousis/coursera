# python3


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
    # Keep list of all existing (i.e. not deleted yet) contacts.
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

