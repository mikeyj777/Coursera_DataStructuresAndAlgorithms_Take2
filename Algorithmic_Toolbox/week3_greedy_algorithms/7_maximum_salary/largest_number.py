#Uses python3

import sys

def isgreaterthanorequal(a, b):
    return int(str(a) + str(b)) > int(str(b) + str(a))

def largest_number(a):
    # LargestNumber(Digits):
    # answer ← empty string

    ans = ''

    for i in range(1, len(a)):
        j = i - 1
        if isgreaterthanorequal(a[j], a[i]):
            ans += str(a[j])
            ans += str(a[i])
        else:
            ans += str(a[i])
            ans += str(a[j])
    
    return ans

    

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
