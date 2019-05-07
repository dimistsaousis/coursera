# python3
import sys


def prepare(distance, tank, stops):
    stops = [0]+stops+[distance]
    return compute(tank, stops)


# with distance appended to stops
def compute(tank, stops, refills=0):
    # sitting on the destination
    if len(stops) == 1:
        return refills

    # impossible to reach destination
    if stops[1] > stops[0]+tank:
        return -1

    # reached destination no refill
    if stops[-1] <= stops[0]+tank:
        return refills

    # find farthest possible stop
    for n in range(2, len(stops)):
        if stops[n] > stops[0]+tank:
            n -= 1
            break

    refills += 1
    stops = stops[n:]

    return compute(tank, stops, refills)


if __name__ == '__main__':
    # distance = 500
    # tank = 200
    # stops = [100, 200, 300, 400]
    # print(prepare(distance, tank, stops))

    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(prepare(d, m, stops))
