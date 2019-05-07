# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(seg):
    seg = sorted(seg, reverse=True)
    points = []

    while len(seg) > 0:
        s = seg.pop(0)
        point = s.start
        points.append(point)
        n = 0
        while len(seg) > 0 and n < len(seg):
            if seg[n].start <= point <= seg[n].end:
                seg.pop(n)
            else:
                n += 1

    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
