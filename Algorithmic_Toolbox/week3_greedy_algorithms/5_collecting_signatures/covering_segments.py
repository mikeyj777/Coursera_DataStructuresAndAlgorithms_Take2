# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

visits = []

# def check_intersections(seg1, seg2):
#     intersxn = set(seg1).intersection(seg2)
#     if len(intersxn) > 0:

def optimal_points(segments):
    segs = []
    #write your code here

    for i in segments:
        seg = []
        for j in range(i.start,i.end+1):
            seg.append(j)
        segs.append(seg)
    
    segs.sort()
    
    winners = []
    i = 0
    while i < len(segs)-1:
        intersxn = set(segs[i]).intersection(segs[i+1])
        winner = intersxn
        j = i + 1
        while len(intersxn) > 0 and j < len(segs) - 1:
            winner = intersxn
            j += 1
            intersxn = set(intersxn).intersection(segs[j])
        if len(winner) > 0:
            winners.append(max(winner))
        else:
            winners.append(max(segs[i]))
        i = max(i+1, j)

    return winners

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
