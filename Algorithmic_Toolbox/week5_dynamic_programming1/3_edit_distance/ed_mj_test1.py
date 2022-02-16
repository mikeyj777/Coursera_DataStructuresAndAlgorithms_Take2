import numpy as np

def edit_distance(a, b):
    a = a.lower()
    b = b.lower()
    n = len(a)
    m = len(b)
    D = np.zeros((n + 1, m + 1))
    
    for j in range(1, m + 1):
        D[0,j] = j

    for i in range(1, n + 1):
        D[i,0] = i


    for j in range(1, m + 1):
        for i in range(1, n + 1):
            insertion = D[i, j - 1] + 1 
            deletion = D[i - 1, j] + 1
            match = D[i-1, j-1]
            mismatch = D[i-1, j-1] + 1
        
            if a[i-1] == b[j-1]:
                D[i,j] = min(insertion, deletion, match)
            else:
                D[i,j] = min(insertion, deletion, mismatch)
    
    return int(D[n, m])

a = "editing"
b = "distance"

e_dist = edit_distance(a, b)

print(e_dist)