# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)-1
    while True:
        mid = int(left + (right-left)/2)
        if right - left <= 1:
            if a[mid] == x:
                return mid
            else:
                return -1
        if a[left] > x:
            return -1
        if a[right] < x:
            return -1
        if a[mid] == x:
            return mid
        if a[mid] < x:
            left = mid
        if a[mid] > x:
            right = mid
    

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    # data = [5, 1, 5, 8, 12, 13, 5, 8, 1, 23, 1, 11]
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x))
