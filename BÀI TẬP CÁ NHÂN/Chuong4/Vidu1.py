def Nhap():
    print('Nhap mot so nguyen:')
    n=int(input('n='))
    return n
def Tinh(n):
    S=0
    for x in range(1,n+1):
        S+=x
    return S
def inKQ(n,S):
    print('Tong cua ',n,' so nguyen duong dau tien= ',S,sep='')
#Lời gọi hàm
a=Nhap()
S=Tinh(a)
inKQ(a,S)