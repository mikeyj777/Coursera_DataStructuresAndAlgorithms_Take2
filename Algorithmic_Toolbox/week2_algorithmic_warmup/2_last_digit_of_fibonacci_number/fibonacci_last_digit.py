# Uses python3
import sys

# def get_fibonacci_last_digit_naive(n):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current

#     return current % 10

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n = int(input)
#     print(get_fibonacci_last_digit_naive(n))

fib_dict = {}

if __name__ == '__main__':
    input_n = int(input())
    fib_dict[0] = 0
    fib_dict[1] = 1
    for i in range(2,input_n+1):
        fib_dict[i] = (fib_dict[i-1] + fib_dict[i-2]) % 10
    print(fib_dict[i])