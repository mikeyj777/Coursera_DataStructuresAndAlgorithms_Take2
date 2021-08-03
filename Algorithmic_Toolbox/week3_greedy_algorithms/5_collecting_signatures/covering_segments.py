# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')



def optimal_points(segments):
    segs_outer = []
    
    #write your code here
    for i in segments:
        # points.append(s.start)
        # points.append(s.end)
        segs_inner = []
        for j in range(i.start, i.end+1):
            segs_inner.append(j)
        segs_outer.append(segs_inner)
    
    for i in range(len(segs_outer)):
        for j in range(len(segs_outer)):
            if i != j:
                for ii in segs_outer[i]:
                    for jj in segs_outer[j]:
                        if ii == jj:
                            
        
        


    return None

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
