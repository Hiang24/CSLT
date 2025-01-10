n=int(input('n='))
if n>=1:
    for i in range(1,n+1):
        print(i,end=' ')
        if i%5==0:
            print(sep='')