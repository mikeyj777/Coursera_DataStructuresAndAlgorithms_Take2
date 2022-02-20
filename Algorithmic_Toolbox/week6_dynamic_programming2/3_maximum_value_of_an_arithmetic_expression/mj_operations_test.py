def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def times(a, b):
    return a * b

ops = [minus, plus, times, minus, plus]

M = [5, 8, 7, 4, 8, 9]

for i in range(1,len(M)):
    for op in ops:
        print(f'{M[i-1]} {op.__name__} {M[i]} = ', op(M[i-1], M[i]))