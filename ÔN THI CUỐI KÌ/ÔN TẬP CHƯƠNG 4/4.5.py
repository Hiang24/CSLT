def LaSoNguyenTo(x):
    dem = 0
    for i in range(1,x+1):
        if x%i==0:
            dem+=1
    if dem==2:
        return True
    else:
        return False
def SoHopLe(x):
    if x<=1:
        return True
    else:
        return False
def NhapVaDem():
    kq = 0
    print('Nhap day so:')
    while True:
        x=int(input())
        if SoHopLe(x) == True:
            break
        if LaSoNguyenTo(x) == True:
            kq += 1
    return kq
def InKQ(kq):
    print(f'Co {kq} so nguyen to')
x=NhapVaDem()
kq=InKQ(x)  