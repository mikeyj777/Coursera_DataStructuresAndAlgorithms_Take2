import numpy as np
import copy

val_hash = {}

val_hash[0] = 0

def knapsack(wts, values, w):
    global val_hash
    if w in val_hash.keys():
        return val_hash[w]
    value_w = 0

    for i in range(1, len(values)+1):
        if wts[i-1] <= w:
            val = knapsack(wts, values, w - wts[i-1]) + values[i-1]

            if val > value_w:
                value_w = val
    val_hash[w] = value_w

    return value_w

w = [6, 3, 4, 5]
v = [30, 14, 16, 9]

capacity = 10

output = knapsack(w, v, capacity)

print(output)
