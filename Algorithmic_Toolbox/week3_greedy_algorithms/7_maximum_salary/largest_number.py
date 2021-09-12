#Uses python3

import sys

def isgreaterthanorequal(a, b):
    return int(str(a) + str(b)) >= int(str(b) + str(a))

def largest_number(a):

    a.sort(reverse = True)

    ans = ''

    for i in range(len(a)):
        if isgreaterthanorequal(ans, a[i]):
            ans += str(a[i])
        else:
            ans = str(a[i]) + ans
    
    return ans

    

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
