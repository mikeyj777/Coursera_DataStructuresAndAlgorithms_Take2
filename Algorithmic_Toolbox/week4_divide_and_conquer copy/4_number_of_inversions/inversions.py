# Uses python3
import sys

num_inversions = 0

def my_sort(a, left, right):
    num_inversions = 0
    if len(a) < 2:
        return a, 0
    i = left - 1
    while i < right:
        i += 1
        for j in range(i + 1, right + 1):
            if i != j:
                if a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]
                    # print(a)
                    num_inversions += 1
                    i = left -1
                    break

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

def merge_sort(arr):
    # code from https://www.geeksforgeeks.org/merge-sort/
    global num_inversions
    if len(arr) > 1:

         # Finding the mid of the array
        mid = len(arr)//2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        merge_sort(L)

        # Sorting the second half
        merge_sort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
                num_inversions += 1
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
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # a = [2, 4, 3, 6, 1]
    
    # print(a)

    merge_sort(a, 0, len(a) - 1)

    # print(f'there were {num_inversions} inversion(s).  The sorted array is {a}.')

    print(num_inversions)
