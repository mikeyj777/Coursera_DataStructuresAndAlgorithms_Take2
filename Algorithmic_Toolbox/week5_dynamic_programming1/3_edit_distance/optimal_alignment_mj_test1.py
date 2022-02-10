from turtle import back
import numpy as np
import copy

#mm ~ match / mismatch
#ins ~ insertion
#del ~ deletion
D = []
def alignment_table(a, b):
    global backtrack, D
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

def output_alignment(a, b, output = []):
    if len(a) == 0 and len(b) == 0:
        return output
    i = len(a) - 1
    j = len(b) - 1
    a_out = ''
    b_out = ''
    if i >= 0:
        a_out = a[i]
    if j >= 0:
        b_out = b[j]
    if i >= 0 and D[i + 1, j + 1] == D[i, j  +1] + 1:
        output = output_alignment(a[:-1], b, output)
        # output.append([a_out, '-'])
        output.append([a[i], '-'])
    elif j >= 0 and D[i + 1, j + 1] == D[i + 1, j] + 1:
        output = output_alignment(a, b[:-1], output)
        # output.append(['-', b_out])
        output.append(['-', b[j]])
    else:
        output = output_alignment(a[:-1], b[:-1], output)
        # output.append([a_out, b_out])
        output.append([a[i], b[j]])
    
    return output


a = "editing"
b = "distance"

alignment_table(a, b)

the_oa = output_alignment(a, b)
the_oa = np.asarray(the_oa)

print(the_oa.T)