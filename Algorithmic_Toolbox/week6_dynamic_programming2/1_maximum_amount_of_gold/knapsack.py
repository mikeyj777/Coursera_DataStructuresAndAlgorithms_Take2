# Uses python3
import sys
import numpy as np

def optimal_weight(W, wts):

    n = len(wts)

    value = np.zeros((W+1, n+1))

    #take the napsack without repetitions model and apply it here.

    for i in range(1, n + 1):
        for w in range(1, W+1):
            value[w, i] = value[w, i-1]
            if wts[i-1] <= w:
                val = value[w - wts[i-1], i - 1] + wts[i-1]
                # print(f'w: {w}.  i: {i}.  wts[i]: {wts[i]}.  value[w, i]: {value[w, i]}.  value[w - wts[i], i-1]:{value[w - wts[i], i-1]}.  val: {val}')
                if val > value[w, i]:
                    value[w, i] = val
    
    return int(value[W, n])
                
W = 20
w = [5, 7, 12, 18]

# W = 3
# w = [1,2]

if __name__ == '__main__':
    # input = sys.stdin.read()
    # W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))