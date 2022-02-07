import math
import copy

class Point:
    def __init__(self, xy):
        self.x = xy[0]
        self.y = xy[1]

def compare_x(p1, p2):

    if p1.x == p2.x:
        return p1.y - p2.y

    return p1.x - p2.x

def compare_y(p1, p2):

    if p1.y == p2.y:
        return p1.x - p2.x

    return p1.y - p2.y

def dist(p1, p2):
    
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def brute_force(p, n):

    the_min = 1e10
    for i in range(n):
        for j in range(i+1, n):
            d = dist(p[i] , p[j])
            if d < the_min:
                the_min = d
    
    return the_min

def strip_closest(strip, size, d):
    
    the_min = d
    
    for i in range(size):
        j = i + 1
        while j < size and (strip[j].y -
                            strip[i].y) < min_val:
            min_val = dist(strip[i], strip[j])
            j += 1
 
    return min_val

def closest_util(px, py, n):
    
    if n <= 3:
        return brute_force(px, n)

    mid_pt = n // 2
    midpoint = px[mid_pt]

    li = 0
    ri = 0

    pyl = []
    pyr = []

    for i in range(n):
        if (py[i].x < midpoint.x or (py[i].x == midpoint.x and py[i].y < midpoint.y)) and li < mid_pt:
            pyl.append(py[i])
            li += 1
        else:
            pyr.append(py[i])
            ri += 1

    dl = closest_util(px, pyl, mid_pt)
    dr = closest_util([x + mid_pt for x in px], pyr, n - mid_pt)

    d = min(dl, dr)

    strip = []

    for i in range(n):
        if abs(py[i].x - midpoint.x) < d:
           strip.append(py[i])
    
    return strip_closest(strip, len(strip) - 1, d)

def closest(p, n):
    px = copy.deepcopy(p)
    py = copy.deepcopy(p)

    px.sort(key=lambda var: var.x)
    py.sort(key=lambda var: var.y)

    return closest_util(px, py, n)

inarr = [[2, 3], [12, 30], [40, 50], [5, 1], [12, 10], [3, 4]]

p = []

p.append([Point(elem) for elem in inarr])

closer = closest(p, len(p))