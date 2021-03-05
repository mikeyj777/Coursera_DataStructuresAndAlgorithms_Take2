# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here

    stops.sort
    stops.append(distance)

    n = len(stops)-2

    numRefills = 0
    currRefill = 0
    while currRefill <= n:
        lastRefill = currRefill
        while currRefill <= n and (stops[currRefill+1] - stops[lastRefill] <= tank):
                currRefill += 1
    
        if currRefill == lastRefill:
            return -1
        
        if currRefill <= n:
            numRefills += 1

    return numRefills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
