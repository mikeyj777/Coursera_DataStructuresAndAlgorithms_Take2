# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    
    elems = {}

    n = (right - left) + 1
    if left == 0:
        n -= 1

    for i in range(len(a)):
        if a[i] in elems.keys():
            elems[a[i]] += 1
            if elems[a[i]] >= n / 2:
                return 1
        else:
            elems[a[i]] = 1

    return -1

if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *a = list(map(int, input.split()))
    a = [2, 3, 9, 2, 2]
    n = len(a)
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
