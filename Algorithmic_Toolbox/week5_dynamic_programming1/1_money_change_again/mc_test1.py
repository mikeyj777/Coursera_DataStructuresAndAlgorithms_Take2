import numpy as np

def dpChange(money, coins):
    min_num_coins = np.zeros((money+1))
    for m in range(1,len(min_num_coins)):
        min_num_coins[m] = np.inf
        for coin in coins:
            if m >= coin:
                num_coins = min_num_coins[m - coin] + 1
                min_num_coins[m] = min(min_num_coins[m], num_coins)
    
    return min_num_coins[money]

a = dpChange(997, [2, 4, 8])

print(a)
