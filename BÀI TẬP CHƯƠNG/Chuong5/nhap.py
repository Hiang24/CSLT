m,n = input().split()
m=int(m)
n = int(n)
L=[[0 for i in range(0,m)] for i in range(0,m)]
for i in range(1,n+1):
    x,y = input().split()
    x = int(x)
    y = int(y)
    L[x-1][y-1] = L[y-1][x-1] = 1
    
for i in range(0,m):
    for j in range(0,m):
        print(L[i][j], end=" ")
    print()
    