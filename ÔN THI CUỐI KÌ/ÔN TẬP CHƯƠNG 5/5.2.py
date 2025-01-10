def Input():
    n=int(input('n='))
    L=[]
    for i in range(n):
        a=int(input())
        L.append(a)
    return n,L
def Search(L):
    L.sort()
    min = L[0]
    max = L[-1]
    return min,max
def Output(max,min):
    print(f'{max} {min}')
n,L=Input()
min,max=Search(L)
Output(max,min)