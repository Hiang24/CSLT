def Nhap(): #Nhập số nguyên n
    n=int(input('n='))
    return n
def NhapVaDem(n):#Nhập n số nguyên
    print('Nhap',n,'so nguyen:')
    d=0
    for i in range(1,n+1):
        x=int(input())
        if x%2==0 and x!=0:
            d+=1
    return d
def InKQ(kq): #In kết quả lên màn hình
    print('So chu so chan la:',kq)

n=Nhap()
ketqua=NhapVaDem(n)
InKQ(ketqua)
