a=str(input())
n=int(input())
if n>=1 and n<=20:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(a,end=" ")
        print("")