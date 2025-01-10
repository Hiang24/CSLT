x=int(input())
def Input():
    n=int(input())
    L=[]
    for i in range(n):
        a=int(input())
        L+=[a]
    return L
def delete(L,x):
    i = 0
    while i < len(L):
        if L[i] == x:
            L.pop(i)
        else:
            i += 1
    return L
L=Input()
print(delete(L,x))