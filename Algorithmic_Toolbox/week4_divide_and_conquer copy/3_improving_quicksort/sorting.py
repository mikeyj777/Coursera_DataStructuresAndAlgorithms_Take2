# Uses python3
import sys
import random

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def partition3(l, r):
    global a
    x = a[l]
    lessers = []
    equals = [x]
    greaters = []
    for i in range(l+1, r+1):
        if a[i] < x:
            lessers.append(a[i])
        if a[i] == x:
            equals.append(x)
        if a[i] > x:
            greaters.append(a[i])
    
    m1 = len(lessers)
    m2 = m1 + len(equals) - 1

    a = lessers + equals + greaters

    return (m1, m2)

def randomized_quick_sort(l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    (m1, m2) = partition3(l, r)
    randomized_quick_sort(l, m1 - 1)
    randomized_quick_sort(m2 + 1, r)


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *a = list(map(int, input.split()))
    a = [2, 1, 3, 2]
    n = len(a)
    randomized_quick_sort(0, n - 1)
    for x in a:
        print(x, end=' ')
