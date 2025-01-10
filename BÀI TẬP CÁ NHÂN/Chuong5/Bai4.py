def Input():
    n=int(input())
    L=[]
    for i in range(n):
        x=int(input())
        L+=[x]
    return L
def count(L):
    dem = 0
    for i in L:
        dem+=1
    return dem
L=Input()
print(count(L))