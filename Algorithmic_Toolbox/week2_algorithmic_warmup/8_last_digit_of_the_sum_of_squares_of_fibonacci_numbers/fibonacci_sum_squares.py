# Uses python3
# from sys import stdin

# def fibonacci_sum_squares_naive(n):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1
#     sum      = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         sum += current * current

#     return sum % 10

# if __name__ == '__main__':
#     n = int(stdin.read())
#     print(fibonacci_sum_squares_naive(n))


import copy

fib_dict = {}
fib_dict[0] = 0
fib_dict[1] = 1

def fib_last_dig_sum_sq(n):
    global fib_dict

    for i in range(2,n+2):
        fib_dict[i] = (fib_dict[i-1] + fib_dict[i-2]) % 10
    
    return (fib_dict[n] * fib_dict[n+1]) % 10
    

if __name__ == '__main__':
    input_n = int(input())
    # n, m = [int(x) for x in input().split()]
    if input_n < 2:
        print(input_n)
    else:
        for i in range(2,input_n+1):
            print(fib_last_dig_sum_sq(i))
        # print(fib_last_dig_sum_sq(input_n))