fib_dict = {}

if __name__ == '__main__':
    input_n = int(input())
    fib_dict[0] = 0
    fib_dict[1] = 1
    for i in range(2,input_n+1):
        fib_dict[i] = fib_dict[i-1]  + fib_dict[i-2]
    print(fib_dict[i])