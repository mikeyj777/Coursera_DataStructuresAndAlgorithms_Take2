# Uses python3
import sys
from random import randint
from datetime import datetime as dt
import copy

num_inversions = 0

def my_sort(a, left, right):
    # bubble sort from https://www.geeksforgeeks.org/bubble-sort/
    num_inversions = 0
    if len(a) < 2:
        return a, 0
    
    isSorted = False
    lastUnsorted = right
    while not isSorted:
        isSorted = True
        for i in range(left, lastUnsorted):
            if a[i] > a[i+1]:
                num_inversions += 1
                a[i], a[i+1] = a[i+1], a[i]
                # print(a)
                isSorted = False
        lastUnsorted -= 1

    return a, num_inversions

# def merge_sort(a, left, right):
#     num_inversions = 0
#     if right - left < 1:
#         return a, 0
#     if right - left == 1:
#         return my_sort(a, left, right)
    
#     ave = (left + right) // 2

#     a, left_invs = merge_sort(a, left, ave - 1)
    
#     a, right_invs = merge_sort(a, ave, right)

#     num_inversions += left_invs + right_invs

#     a, more_invs = my_sort(a, left, right)

#     return a, num_inversions + more_invs

def mergeSort(arr):
    if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        mergeSort(L)
  
        # Sorting the second half
        mergeSort(R)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1



if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *a = list(map(int, input.split()))
    # a = [2, 3, 9, 2, 9]
    a = []
    a = [77, 65, 52]
    
    # for i in range(int(6)):
    #     a.append(randint(1, 100))
    
    a0 = copy.deepcopy(a)
    
    b = [0] * len(a)
    # print(a)
    t0 = dt.now()
    mergeSort(a)

    # print(f'there were {num_inversions} inversion(s).  The sorted array is {a}.')
    print(a0, a, a == sorted(a0), num_inversions, dt.now() - t0)
    
    pass