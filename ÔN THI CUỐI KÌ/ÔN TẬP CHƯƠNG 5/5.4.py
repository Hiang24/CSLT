n=int(input('n='))
L=[]
for i in range(n):
    a=int(input())
    L.append(a)
M = L[::-1]
L.sort()
print(M)
print(L)