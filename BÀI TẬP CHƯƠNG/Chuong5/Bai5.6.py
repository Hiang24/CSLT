A=[]
for j in range(10):
    x=int(input())
    A.append(x)
B=A[:] #Sao chép A qua B
for i in range(0,len(A),2):
    B[i]=A[i+1]
    B[i+1]=A[i]
for x in B:
    print(x,end=' ')