n=int(input("n="))
i=1
if n>=1 and n<=50:
    while i<=n:
        print(i,end=" ")
        i=i+1
        if (i-1)%10==0:
            print(sep="")