# Uses python3
import sys
import numpy as np

def optimal_weight(W, wts):

    value = np.zeros((W+1))

    for w in range(1, W+1):
        for i in range(len(wts)):
            for j in range(len(wts)):
                if wts[i] <= w and wts[j] <= w and i != j:
                    val = value[w - wts[i]] + wts[j]
                    if val > value[w] and val <= W:
                        value[w] = val
    
    return value[W]
                


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
