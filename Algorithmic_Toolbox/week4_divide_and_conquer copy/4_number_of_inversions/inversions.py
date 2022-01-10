# Uses python3
import sys
from random import randint
from datetime import datetime as dt

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

def merge_sort(a, left, right):
    num_inversions = 0
    if right - left < 1:
        return a, 0
    if right - left == 1:
        return my_sort(a, left, right)
    
    ave = (left + right) // 2

    a, left_invs = merge_sort(a, left, ave - 1)
    
    a, right_invs = merge_sort(a, ave, right)

    num_inversions += left_invs + right_invs

    a, more_invs = my_sort(a, left, right)

    return a, num_inversions + more_invs


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *a = list(map(int, input.split()))
    # a = [2, 3, 9, 2, 9]
    a = []
    for i in range(100000):
        a.append(randint(1, 100))
    
    # print(a)
    t0 = dt.now()
    a, num_inversions = merge_sort(a,0, len(a)-1)

    # print(f'there were {num_inversions} inversion(s).  The sorted array is {a}.')

    print(num_inversions, dt.now() - t0, a == sorted(a))
