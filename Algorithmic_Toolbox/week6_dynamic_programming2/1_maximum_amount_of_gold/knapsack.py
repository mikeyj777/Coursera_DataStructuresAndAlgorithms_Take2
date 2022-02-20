# Uses python3
import sys
import numpy as np

def optimal_weight(W, wts):

    value = np.zeros((W+1))

    #take the napsack without repetitions model and apply it here.

    for w in range(1, W+1):
        for i in range(len(wts)):
            if wts[i] <= w:
                val = value[w - wts[i]] + wts[i]
                print(f'w: {w}.  i: {i}.  wts[i]: {wts[i]}.  value[w]: {value[w]}.  value[w - wts[i]]:{value[w - wts[i]]}.  val: {val}')
                if val > value[w]:
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