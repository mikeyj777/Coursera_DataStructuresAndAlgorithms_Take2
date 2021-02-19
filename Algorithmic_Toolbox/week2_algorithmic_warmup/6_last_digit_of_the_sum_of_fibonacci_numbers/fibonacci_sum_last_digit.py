# # Uses python3
# import sys

# def fibonacci_sum_naive(n):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1
#     sum      = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         sum += current

#     return sum % 10

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n = int(input)
#     print(fibonacci_sum_naive(n))

import copy

fib_dict = {}
fib_dict[0] = 0
fib_dict[1] = 1

def fib_sum_last_dig(n):
    global fib_dict

    ans = 1

    for i in range(2,n+1):
        fib_dict[i] = (fib_dict[i-1] + fib_dict[i-2]) % 10
        ans += fib_dict[i]
        ans %= 10
    
    return ans
    

if __name__ == '__main__':
    input_n = int(input())
    # n, m = [int(x) for x in input().split()]
    # if input_n < 2:
    #     print(input_n)
    # else:
    #     for i in range(2,input_n+1):
    #         print(fib_sum_last_dig(i))
    if input_n <= 2:
        if input_n < 2:
            print(input_n)
        else:
            print(2)
    else:
        print(fib_sum_last_dig(input_n))
