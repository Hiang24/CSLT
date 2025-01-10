def nhap():
    n = int(input('n='))
    return n
def giaithua(n):
    X=1
    for i in range(1,n+1):
        X*=i
    return X
def inkq(n,X):
    print(f'{n}!={X}')
n=nhap()
X=giaithua(n)
inkq(n,X)
    