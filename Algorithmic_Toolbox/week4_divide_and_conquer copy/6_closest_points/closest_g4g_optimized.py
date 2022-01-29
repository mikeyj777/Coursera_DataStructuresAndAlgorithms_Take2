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