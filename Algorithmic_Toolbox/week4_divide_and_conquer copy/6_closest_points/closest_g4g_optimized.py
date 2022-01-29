import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

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

    mid = n // 2
    midpoint = px[mid]

    li = 0
    ri = 0

    for i in range(n):
        if (py[i].x < midpoint.x or (py[i].x == midpoint.x and py[i].y < midpoint.y)) and li < mid:
            li++
    {
      if ((Py[i].x < midPoint.x || (Py[i].x == midPoint.x && Py[i].y < midPoint.y)) && li<mid)
         Pyl[li++] = Py[i];
      else
         Pyr[ri++] = Py[i];
    }