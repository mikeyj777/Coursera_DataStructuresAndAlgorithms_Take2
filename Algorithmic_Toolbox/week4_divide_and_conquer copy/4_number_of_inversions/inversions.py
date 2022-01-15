# Uses python3
import sys
from random import randint
from datetime import datetime as dt
import copy

num_inversions = 0
a0 = []
#iterative merge sort:  https://www.geeksforgeeks.org/iterative-merge-sort/


# perform bottom up merge
def mergeSort(a):
    # start with least partition size of 2^0 = 1
    width = 1   
    n = len(a)                                         
    # subarray size grows by powers of 2
    # since growth of loop condition is exponential,
    # time consumed is logarithmic (log2n)
    while (width < n):
        # always start from leftmost
        l=0
        while (l < n):
            r = min(l+(width*2-1), n-1)
            m = (l+r)//2
            # final merge should consider
            # unmerged sublist if input arr
            # size is not power of 2
            if (width>n//2):       
                m = r-(n%width)  
            merge(a, l, m, r)
            l += width*2
        # Increasing sub array size by powers of 2
        width *= 2
    return a
   
# Merge Function
def merge(a, l, m, r):
    global a0, num_inversions
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = a[l + i]
    for i in range(0, n2):
        R[i] = a[m + i + 1]
 
    i, j, k = 0, 0, l
    while i < n1 and j < n2:
        if L[i] > R[j]:
            a[k] = R[j]
            num_inversions += 1
            j += 1
        else:
            a[k] = L[i]
            i += 1
        # if a0[k] > a[k]:
        #     num_inversions += 1
        k += 1
 
    while i < n1:
        a[k] = L[i]
        # if a0[k] > a[k]:
        #     num_inversions += 1
        i += 1
        k += 1
 
    while j < n2:
        a[k] = R[j]
        # if a0[k] > a[k]:
        #     num_inversions += 1
        j += 1
        k += 1



if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *a = list(map(int, input.split()))
    a = [2, 3, 9, 2, 9]
    # a = []
    # a = [77, 65, 52]
    
    # for i in range(int(6)):
    #     a.append(randint(1, 100))
    
    a0 = copy.deepcopy(a)
    
    # b = [0] * len(a)
    # print(a)

    t0 = dt.now()
    mergeSort(a)

    # print(f'there were {num_inversions} inversion(s).  The sorted array is {a}.')
    print(a0, a, a == sorted(a0), num_inversions, dt.now() - t0)
    
    pass