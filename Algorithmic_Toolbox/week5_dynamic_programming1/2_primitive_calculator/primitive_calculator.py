# Uses python3
import sys
import copy
import numpy as np

winners = []
def calculator(target, n=1, calc_chain = []):
    global winners
    calc_chain.append(n)
    if n == target:
        winners.append(calc_chain)
    if n < target:
        inputs = [n + 1, n * 2, n * 3]
        if min(inputs) <= target:
            for inp in inputs:
                if inp <= target:
                    
                    if calc_chain == [1, 2, 2]:
                        apple = 1
                    calculator(target, inp, copy.deepcopy(calc_chain))

def calc_handler(n):
    calculator(n)
    shortest_chain = np.inf
    shortest_idx = -1
    for i in range(len(winners)):
        if len(winners[i]) < shortest_chain:
            shortest_chain = len(winners[i])
            shortest_idx = i
    return winners[shortest_idx]




# input = sys.stdin.read()
# n = int(input)

n = 0

output = calc_handler(n)
print(len(output) - 1)
for x in output:
    print(x, end=' ')
