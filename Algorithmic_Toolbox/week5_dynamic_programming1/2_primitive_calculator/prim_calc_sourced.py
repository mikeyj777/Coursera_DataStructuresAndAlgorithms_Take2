import sys

#  http://thisthread.blogspot.com/2018/02/primitive-calculator.html

def calculator(target):

    cache = [0] * (target + 1)  # 1
    for i in range(1, len(cache)):  # 2
        cache[i] = cache[i-1] + 1
        if i % 2 == 0:
            cache[i] = min(cache[i], cache[i // 2] + 1)
        if i % 3 == 0:
            cache[i] = min(cache[i], cache[i // 3] + 1)

    result = [1] * cache[-1]  # 1
    for i in range(1, cache[-1]):  # 2
        result[-i] = target  # 3
        if cache[target-1] == cache[target] - 1:  # 4
            target -= 1
        elif target % 2 == 0 and (cache[target // 2] == cache[target] - 1):  # 5
            target //= 2
        else:  # 6 # target % 3 == 0 and (cache[target // 3] == cache[target] - 1):
            target //= 3
    
    return result

input = sys.stdin.read()
n = int(input)

output = calculator(n)
print(len(output) - 1)
for x in output:
    print(x, end=' ')
