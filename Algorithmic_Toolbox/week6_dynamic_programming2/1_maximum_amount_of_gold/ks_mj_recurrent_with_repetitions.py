import numpy as np

def knapsack(wts, vals, W):

    value = np.zeros((W+1))

    for w in range(1, W+1):
        for i in range(len(wts)):
            if wts[i] <= w:
                val = value[w - wts[i]] + vals[i]
                if val > value[w]:
                    value[w] = val
    
    return value[W]
                

w = [6, 3, 4, 5]
v = [30, 14, 16, 9]

capacity = 10

output = knapsack(w, v, capacity)

print(output)