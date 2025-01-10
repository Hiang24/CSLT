n=int(input("n="))
if 0<=n<=100:
    a=1
    for i in range(n,0,-1):
        a=a*i
    print('{}!={}'.format(n,a))