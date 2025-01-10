x=int(input())
y=int(input())
def Input():
    n=int(input())
    L=[]
    for i in range(n):
        x=int(input())
        L+=[x]
    return L
def update(L,x,y):
    for i in range(len(L)):
        if L[i]==x:
            L[i]=y
    return L
L=Input()
print(update(L,x,y))