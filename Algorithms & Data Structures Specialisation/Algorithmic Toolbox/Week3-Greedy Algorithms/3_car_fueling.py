"""
Input Format.
The first line contains an integer 𝑑.
The second line contains an integer 𝑚.
The third line specifies an integer 𝑛.
Finally, the last line contains integers stop1,stop2, . . . ,stop𝑛.

Output Format. Assuming that the distance between the cities is 𝑑 miles, a car can travel at most 𝑚 miles
on a full tank, and there are gas stations at distances stop1,stop2, . . . ,stop𝑛 along the way, output the
minimum number of refills needed. Assume that the car starts with a full tank. If it is not possible to
reach the destination, output −1.

Constraints. 1 ≤ 𝑑 ≤ 105. 1 ≤ 𝑚 ≤ 400. 1 ≤ 𝑛 ≤ 300. 0 < stop1 < stop2 < · · · < stop𝑛 < 𝑚.
"""


def pre_process(distance, tank, stops):
    stops = [0]+stops+[distance]
    return get_minimum_number_of_refills(tank, stops)


# with distance appended to stops
def get_minimum_number_of_refills(tank, stops, refills=0):
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
    n = 2
    while stops[n] > stops[0]+tank and n < len(stops):
        n += 1

    n -= 1

    refills += 1
    stops = stops[n:]

    return get_minimum_number_of_refills(tank, stops, refills)


if __name__ == '__main__':
    d, m, _, *s = map(int, input().split())
    print(pre_process(d, m, s))
