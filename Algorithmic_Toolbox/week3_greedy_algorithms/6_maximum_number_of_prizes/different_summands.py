# Uses python3
import sys

def optimal_summands(n):
    summands = {}
    
    ans = n

    if n < 3:
        summands[n] = ''
        
        return list(summands.keys())

    for i in range(1,n):
        if (ans - i) not in summands.keys() and i < ans and ans - i != i:
            ans -= i
            summands[i] = ''
        else:
            summands[ans] = ''
            break
        


    return list(summands.keys())

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
