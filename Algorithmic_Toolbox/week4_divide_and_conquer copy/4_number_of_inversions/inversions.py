# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    for i in range(left,right):
        if a[i] > a[i+1]:
            number_of_inversions += 1
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # a = [0, 1, 0]
    # n = len(a)
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, n - 1))
