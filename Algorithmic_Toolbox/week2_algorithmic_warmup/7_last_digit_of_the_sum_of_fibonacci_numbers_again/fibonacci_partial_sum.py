# # Uses python3
# import sys

# def fibonacci_partial_sum_naive(from_, to):
#     sum = 0

#     current = 0
#     next  = 1

#     for i in range(to + 1):
#         if i >= from_:
#             sum += current

#         current, next = next, current + next

#     return sum % 10


# if __name__ == '__main__':
#     input = sys.stdin.read();
#     from_, to = map(int, input.split())
#     print(fibonacci_partial_sum_naive(from_, to))


import copy

def fib_partial_sum_last_dig(m, n):
    
    fib_dict = {}
    fib_dict[-1] = 0
    fib_dict[-2] = 0
    fib_dict[0] = 0
    fib_dict[1] = 1
    
    ans = 0

    for i in range(0,n+1):
        if i != 1:
            fib_dict[i] = (fib_dict[i-1] + fib_dict[i-2]) % 10
        if i >= m:
            ans += fib_dict[i]
            ans %= 10
    
    return ans
    

if __name__ == '__main__':
    # input_n = int(input())
    f_low, f_high = [int(x) for x in input().split()]
    print(fib_partial_sum_last_dig(f_low, f_high))