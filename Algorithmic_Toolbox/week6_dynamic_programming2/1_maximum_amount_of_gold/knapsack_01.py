# Uses python3
import sys
import numpy as np

def optimal_weight(W, wts):

    value = np.zeros((W+1))

    for w in range(1, W+1):
        for i in range(len(wts)):
            for j in range(len(wts)):
                if wts[i] <= w and wts[j] <= w:
                    val = value[w - wts[i]] + wts[j]
                    print(f'w: {w}.  i: {i}.  j: {j}.  wts[i]: {wts[i]}.  wts[j]: {wts[j]}.  value[w]: {value[w]}.  value[w - wts[i]]:{value[w - wts[i]]}.  val: {val}')
                    if val > value[w] and val <= w:
                        value[w] = val
    
    return int(value[W])
                
W = 20
w = [5, 7, 12, 18]

# W = 3
# w = [1,2]

if __name__ == '__main__':
    # input = sys.stdin.read()
    # W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))