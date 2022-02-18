import numpy as np

def knapsack(wts, values, W):
    n = len(wts)

    value = np.zeros((W + 1, n + 1))

    for i in range(1,n + 1):
        for w in range(1, W+1):
            value[w, i] = value[w, i-1]
            if wts[i-1] <= w:
                val = value[w - wts[i-1], i - 1] + values[i-1]
                if value[w, i] < val:
                    value[w,i] = val
    
    return value[W,n]


w = [6, 3, 4, 5]
v = [30, 14, 16, 9]

capacity = 10

output = knapsack(w, v, capacity)

print(output)
