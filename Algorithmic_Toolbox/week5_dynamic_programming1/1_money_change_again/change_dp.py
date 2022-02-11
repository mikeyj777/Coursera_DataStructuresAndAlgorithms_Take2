# Uses python3
import sys
import numpy as np

def get_change(money):
    coins = [1, 3, 4]
    min_num_coins = np.zeros((money+1))
    for m in range(1,len(min_num_coins)):
        min_num_coins[m] = np.inf
        for coin in coins:
            if m >= coin:
                num_coins = min_num_coins[m - coin] + 1
                min_num_coins[m] = min(min_num_coins[m], num_coins)
    
    return int(min_num_coins[money])

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
