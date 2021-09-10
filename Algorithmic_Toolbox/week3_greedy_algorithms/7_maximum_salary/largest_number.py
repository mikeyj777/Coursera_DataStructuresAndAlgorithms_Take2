#Uses python3

import sys

def largest_number(a):
    #write your code here
    # res = []
    # for x in a:
    #     list_x = list(str(x))
    #     for i in list_x:
    #         res.append(i)
    
    # res.sort(reverse=True)

    # ans = 0

    # currpow = 0

    # for i in range(len(res)-1,-1,-1):
    #     ans += int(res[i])*10**currpow
    #     currpow += 1
    
    # return ans


    res = ""

    a.sort(reverse=True)

    for x in a:
        res += x
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
