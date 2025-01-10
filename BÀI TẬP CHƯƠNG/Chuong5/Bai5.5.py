A=[]
n=int(input('n='))
for j in range(n):
    x=int(input())
    A.append(x)
    tong=0
    for i in range(1,len(A),2):
        tong+=A[i]
print(f'Tong={tong}')