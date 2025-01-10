n=int(input('n='))
L=[]
for i in range(n):
    a=int(input())
    L.append(a)
M = []
for x in L:
    if x not in M:
        M.append(x)
for z in M:
    print(z,end=' ')