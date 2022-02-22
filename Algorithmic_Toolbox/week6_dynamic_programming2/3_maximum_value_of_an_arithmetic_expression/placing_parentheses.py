# Uses python3
import numpy as np

d = []
ops = []
n = len(d)
m = np.zeros((n+1,n+1))
M = np.zeros((n+1,n+1))

def plus(a, b):
    return a + b

def subtract(a, b):
    return a - b

def times(a, b):
    return a * b



def parseinput(a):
    global d, ops
    start_pos = 0
    for i in range(len(a)):
        if not a[i].isnumeric():
            curr_num = a[start_pos:i]
            start_pos = i + 1
            d.append(curr_num)
            opn = a[i]
            if opn == '+':
                ops.append(plus)
            if opn == '-':
                ops.append(subtract)
            if opn == '*':
                ops.append(times)
        if i == len(a) - 1:
            curr_num = a[start_pos:]
            d.append(curr_num)



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
            # print(f's:{s}.  i:{i}. j:{j}.  m[i,j]:{m[i,j]}.  M[i,j]:{M[i,j]}.')
    
    return int(M[1,n])



if __name__ == "__main__":
    a = input()
    parseinput(a)
    n = len(d)
    m = np.zeros((n+1,n+1))
    M = np.zeros((n+1,n+1))

    output = parentheses()

    print(output)

