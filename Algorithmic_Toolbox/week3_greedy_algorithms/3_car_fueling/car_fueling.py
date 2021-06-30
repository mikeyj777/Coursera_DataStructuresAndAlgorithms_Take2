# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here

    stops.sort
    stops.append(distance)

    n = len(stops)

    currPosn = -1
    startingPosn = 0
    numTanks = 0
    while currPosn < n:
        currPosn +=1 
        if stops[currPosn] - stops[startingPosn] > tank:
            startingPosn = currPosn
            numTanks += 1
    
    return numTanks


    

if __name__ == '__main__':
    d, m, _, *s5tops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
