# Uses python3
# import sys

# def get_fibonacci_huge_naive(n, m):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current

#     return current % m

# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n, m = map(int, input.split())
#     print(get_fibonacci_huge_naive(n, m))

import copy

fib_dict = {}
fib_dict[0] = 0
fib_dict[1] = 1

def fib_n_mod_m(n,m):
    global fib_dict

    pisano = copy.deepcopy(fib_dict)

    period = -1

    for i in range(2,n+1):
        fib_dict[i] = (fib_dict[i-1] + fib_dict[i-2])
        pisano[i] = fib_dict[i] % m
        if i > 2:
            if pisano[i] == 1 and pisano[i-1] == 0:
                period = len(pisano)-2
                break
    

    if period < 0:
        return pisano[n]
        
    targ_pisano_idx = int(n % period)

    if targ_pisano_idx < 2:
        return targ_pisano_idx

    ans = pisano[targ_pisano_idx]

    return ans
    

if __name__ == '__main__':
    n, m = [int(x) for x in input().split()]
    if n > 1:
        print(fib_n_mod_m(n,m))
    else:
        print(n)
