x=int(input())
k=int(input())
def Input():
    n=int(input())
    L=[]
    for i in range(n):
        x=int(input())
        L+=[x]
    return L
def add(L,x,k):
    n = len(L)
    if k > n:
        L+=[x]
    else:
        L.insert(k,x)
    return L
L=Input()
print(add(L,x,k))