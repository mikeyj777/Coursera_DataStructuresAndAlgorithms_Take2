# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

visits = []

def optimal_points(segments):
    segs = []
    #write your code here

    for i in segments:
        seg = []
        for j in range(i.start,i.end+1):
            seg.append(j)
        segs.append(seg)
    
    for i in range(len(segs)):
        for j in range(i,len(segs)):
            intersxn = set(segs[i]).intersection(segs[j])
            #recursively check if segs[j] and 'intersxn' have intersecting members.
            #if so check next j
            #if not, store as a time when will need to visit.
                
    
    return None

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
