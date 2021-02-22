# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here

    stops.append(distance)
    stops.sort()
    
    currdist = 0
    
    totstops = 0
    
    i = 0
    while i < len(stops):
        while i < len(stops) and (stops[i] - currdist) <= tank and stops[i] <= distance:
            i += 1
        if i > len(stops):
            break
        currstop = stops[i-1]
        if (currstop - currdist) <= tank:
            if currstop == distance:
                return totstops
            totstops += 1
            currdist = currstop
            if currdist >= distance:
                break
        else:
            return -1
        
    if totstops == 0:
        return -1

    return totstops

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
