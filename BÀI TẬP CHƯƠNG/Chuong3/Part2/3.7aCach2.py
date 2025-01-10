while True:
    n=int(input())
    if n<0:
        break
    elif n==0:
        print('1')
    else:
        a=1
        i=1
        while i<=n:
            a*=i
            i+=1
        print(a)
    
