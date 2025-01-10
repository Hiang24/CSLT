def nhap():
    n=int(input('n='))
    return n
def giaithua(n):
    X=1
    if n>=0:
        i=1
        while i<=n:
            X*=i
            i+=1
        return X
def inkq(n,X):
    print('{}!={}'.format(n,X))
n=nhap()
X=giaithua(n)
inkq(n,X)