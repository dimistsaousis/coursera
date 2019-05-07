"""
Task. You’re in the middle of writing your newspaper’s end-of-year economics summary, and you’ve decided
that you want to show a number of charts to demonstrate how different stocks have performed over the
course of the last year. You’ve already decided that you want to show the price of 𝑛 different stocks,
all at the same 𝑘 points of the year.
A simple chart of one stock’s price would draw lines between the points (0, 𝑝𝑟𝑖𝑐𝑒0),(1, 𝑝𝑟𝑖𝑐𝑒1), . . . ,(𝑘 −
1, 𝑝𝑟𝑖𝑐𝑒𝑘−1), where 𝑝𝑟𝑖𝑐𝑒𝑖
is the price of the stock at the 𝑖-th point in time.
In order to save space, you have invented the concept of an overlaid chart. An overlaid chart is the
combination of one or more simple charts, and shows the prices of multiple stocks (simply drawing a
line for each one). In order to avoid confusion between the stocks shown in a chart, the lines in an
overlaid chart may not cross or touch.
Given a list of 𝑛 stocks’ prices at each of 𝑘 time points, determine the minimum number of overlaid
charts you need to show all of the stocks’ prices.

Input Format. The first line of the input contains two integers 𝑛 and 𝑘 — the number of stocks and the
number of points in the year which are common for all of them. Each of the next 𝑛 lines contains 𝑘
integers. The 𝑖-th of those 𝑛 lines contains the prices of the 𝑖-th stock at the corresponding 𝑘 points
in the year.

Constraints. 1 ≤ 𝑛 ≤ 100; 1 ≤ 𝑘 ≤ 25. All the stock prices are between 0 and 1 000 000.

Output Format. Output a single integer — the minimum number of overlaid charts to visualize all the
stock price data you have.
"""


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
