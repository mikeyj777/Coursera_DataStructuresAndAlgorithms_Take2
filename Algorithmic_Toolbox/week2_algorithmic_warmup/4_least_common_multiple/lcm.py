# Uses python3
import sys

def eulerGcd(a, b):
    if b == 0:
        return a
    a_prime = a % b
    return eulerGcd(b, a_prime)

def lcm(a, b):
    return int(abs(a*b) / eulerGcd(a, b))

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

if __name__ == '__main__':
    # input = sys.stdin.read()
    # a, b = map(int, input.split())
    a, b = [int(x) for x in input().split()]
    print(lcm(a, b))

