# python3
class Stock:
    def __init__(self, idx, data, size):
        self.idx = idx
        self.size = size
        self.data = data
        self.children = dict()
        self.parent = None

    def compare(self, stock):
        if self.data[0] > stock.data[0]:
            for i in range(1, self.size):
                if self.data[i] <= stock.data[i]:
                    return 'Intersect'
            return 'Greater'
        elif self.data[0] < stock.data[0]:
            for i in range(1, self.size):
                if self.data[i] >= stock.data[i]:
                    return 'Intersect'
            return 'Less'


if __name__ == '__main__':
    number_of_stocks, number_of_data_points = map(int, input().split())
    stocks = []
    for stock_no in range(number_of_stocks):
        stock_data = list(map(int, input().split()))
        stocks.append(Stock(stock_no, stock_data, number_of_data_points))
