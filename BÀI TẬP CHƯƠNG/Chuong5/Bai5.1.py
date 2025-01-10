def Input():
    n=int(input('n='))
    L=[]
    for i in range(n):
        x=int(input())
        L+=[x]
    x=int(input("x="))
    return x,L
def FirstAndLast(L):
    daucuoi=[L[0],L[-1]]
    print(daucuoi)
def Search(L,x):
    if x in L:
        return True
    else:
        return False
n,L=Input()
FirstAndLast(L)
print(Search(L,n))



