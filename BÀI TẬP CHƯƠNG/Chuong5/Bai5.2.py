def Input():
    n=int(input('n='))
    L=[]
    for i in range(n):
        x=int(input())
        L+=[x]
    return L
def Search(L):
    L.sort()
    min=L[0]
    max=L[-1]
    return min,max
def Output(min,max):
    print(f'{max} {min}')
L=Input()
min,max= Search(L)
Output(min,max)
