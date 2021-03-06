#Uses python3
import sys
import numpy as np
import math


def pts_dist(p0, p1):

    x0 = p0[0]
    y0 = p0[1]
    x1 = p1[0]
    y1 = p1[1]

    dist = math.sqrt((x1 - x0)**2 + (y1 - y0)**2)

    return dist

def get_min_dist(S, stop_after_x_points = 0):

    if len(S) == 1:
        return 1e10
    
    dists = []
    for i in range(len(S)):
        j_upper = len(S)
        if stop_after_x_points > 0:
            j_upper = min(j_upper, i + stop_after_x_points + 1)
        
        for j in range(i+1, j_upper):
            dist = pts_dist(S[i], S[j])
            if dist == 0:
                return 0
            dists.append(dist)
    
    min_dist = min(dists)

    return min_dist


def minimum_distance(xy):
    
    if len(xy) == 1:
        return 0

    if len(xy) == 2:
        return pts_dist(xy[0], xy[1])

    mid_x = (max(xy[:,0]) + min(xy[:,0])) / 2

    S1 = xy[xy[:,0] < mid_x]
    S2 = xy[xy[:,0] >= mid_x]

    min_dist_1 = get_min_dist(S1)
    min_dist_2 = get_min_dist(S2)
    min_dist = min(min_dist_1, min_dist_2)
    
    if min_dist == 0:
        return 0

    S1 = S1[S1[:,0] < mid_x + min_dist]
    S2 = S2[S2[:,0] < mid_x + min_dist]

    P = np.vstack((S1, S2))
    P = np.asarray(P)
    # P = P[P[:,1].argsort()]
    # P = P[:7]
    min_dist_P = get_min_dist(P, 7)
    the_min = min(min_dist, min_dist_P)
    
    return the_min

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    
    xy = np.asarray([x,y])
    xy = xy.T

    # xy = np.asarray([   [0, 0],
    #                     [5, 6],
    #                     [3, 4],
    #                     [7, 2]])

    # print(xy)

    print("{0:.9f}".format(minimum_distance(xy)))
