def Nhap():
    L=[]
    for i in range(10):
        k=int(input())
        L+=[k]
    x=int(input("x="))
    return x,L
def InKQ(L):
    for x in L:
        print(x,end=', ')
    print()
def CauA(x,L):
    for i in range(len(L)):
        if L[i]==5:
            L[i]=x
    InKQ(L)
# def CauB(x,L):
#     i=0
#     while i<len(L):
#         if L[i]==x:
#             del(L[i])
#         else:
#             i+=1
#     InKQ(L)   

def CauB(x,L):
    for i in range(len(L)):
        if L[i] == x:
            del L[i]
    InKQ(L)     
x,L=Nhap()
CauA(x,L)
CauB(x,L)