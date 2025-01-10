x=int(input())
def Input():
    n=int(input())
    L=[]
    for i in range(n):
        x=int(input())
        L+=[x]
    return L
def search(L,x):
    if x in L:
        return L.index(x)
    else:
        return None
L=Input()
print(search(L,x))