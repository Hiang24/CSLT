A = []
B = []
C = []
n = int(input('n='))
m = int(input('m='))

print('L1:')
for i in range(0,n):
    A.append(int(input()))
    
print('L2:')
for i in range(0,m):
    B.append(int(input()))
    
for i in A:
    if i in B:
        C.append(i)
print('L3:', end=' ')
for i in C:
    print(i, end=' ')
