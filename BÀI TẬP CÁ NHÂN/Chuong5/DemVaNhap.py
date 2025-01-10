import random
def Nhap():
    n=int(input('n='))
    return n
def SinhDaySo(n):
    L=[]
    for i in range(n):
        x=random.randint(-100,100)
        L+=[x]
    return L
def DemVaIn(L):
    dem=0
    for x in L:
        if x%2==0 and x>=10:
            dem+=1
    print('L:',L)
    print('So nguyen chan lon hon bang 10:',dem)
n=Nhap()
L=SinhDaySo(n)
DemVaIn(L)