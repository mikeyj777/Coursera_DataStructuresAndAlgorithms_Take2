def eulerGcd(a, b):
    if b == 0:
        return a
    a_prime = a % b
    return eulerGcd(b, a_prime)

if __name__ == '__main__':
    input_numbers = [int(x) for x in input().split()]
    a = input_numbers[0]
    b = input_numbers[1]
    print(eulerGcd(a,b))