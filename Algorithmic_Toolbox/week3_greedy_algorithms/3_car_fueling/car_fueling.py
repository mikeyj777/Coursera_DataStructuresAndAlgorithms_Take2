# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here

    stops.append(distance)
    if 0 not in stops:
        stops.append(0)
    stops.sort
    
    n = len(stops)

    currPosn = 0
    startingPosn = 0
    numFills = 0
    while currPosn < n-1:
        if stops[currPosn+1] - stops[currPosn] > tank:
            return -1
        if stops[currPosn + 1] - stops[startingPosn] >= tank:
            startingPosn = currPosn + 1
            numFills += 1
        currPosn += 1
    
    return numFills


    

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
