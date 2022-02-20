n = 5

for s in range(1,n):
    for i in range(1,n-s+1):
        j = i + s
        print(f's:{s}.  i:{i}.  j:{j}')