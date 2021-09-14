import numpy as np

def mult2(A,B,n,al,bl):
    r = np.zeros(2*n - 1)
    if n == 1:
        r[0] = A[al] * B[bl]
        return r
    rlow = mult2(A, B, n//2, al, bl)
    rhigh = mult2(A, B, n//2, al + n//2, bl + n//2)
    d0e1 = mult2(A, B, n//2, al, bl + n//2)
    d1e0 = mult2(A, B, n//2, al + n//2, bl)
    rmid = d1e0 + d0e1
    for i in range(len(rlow)):
        r[i] += rlow[i]
    for i in range(len(rhigh)):
        r[i+n] += rhigh[i]
    for i in range(len(rmid)):
        r[n//2 + i] += rmid[i] 
    return r

n = 4

#A(x) = 3x^2 + 2x + 4
#B(x) = 5x^2 + 3x + 2

A = [4, 2, 3, 0]
B = [2, 3, 5, 0]

r = mult2(A,B,n,0,0)

ans = ''
for i in range(len(r)-1,-1,-1):
    ans += str(r[i])
    if i > 0:
        ans += ' * x ^ ' + str(i) + ' + '

print(ans) 