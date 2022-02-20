import numpy as np
import copy

#expression:  5 - 8 + 7 * 4 - 8 + 9
d = [5, 8, 7, 4, 8, 9]
n = len(d)
m = np.zeros((n+1,n+1))
M = np.zeros((n+1,n+1))
def plus(a, b):
    return a + b

def subtract(a, b):
    return a - b

def times(a, b):
    return a * b

ops = [subtract, plus, times, subtract, plus]

def minAndMax(i, j):
    min_ = np.inf
    max_ = -np.inf

    for k in range(i, j):
        op = ops[k-1]

        a = op(M[i, k], M[k+1, j])
        b = op(M[i, k], m[k+1, j])
        c = op(m[i, k], M[k+1, j])
        d = op(m[i, k], m[k+1, j])
        min_ = min(min_, a, b, c, d)
        max_ = max(max_, a, b, c, d)
    
    return min_, max_

def parentheses():
    global m, M
    for i in range(1, n + 1):
        m[i, i] = d[i-1]
        M[i, i] = d[i-1]
    for s in range(1,n):
        for i in range(1, n-s + 1):
            j = i + s
            m[i,j], M[i,j] = minAndMax(i,j)
            print(f's:{s}.  i:{i}. j:{j}.  m[i,j]:{m[i,j]}.  M[i,j]:{M[i,j]}.')
    
    return M[1,n]

a = parentheses()

print(a)


