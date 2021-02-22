# Uses python3
import sys

coins = [10, 5 ,1]

def get_change(m):
    
    remVal = m
    totCoins = 0
    for coin in coins:
        if coin <= remVal:
            currCoins = int(remVal / coin)
            remVal -= currCoins * coin
            totCoins += currCoins
            if remVal < 1:
                break


    return totCoins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
