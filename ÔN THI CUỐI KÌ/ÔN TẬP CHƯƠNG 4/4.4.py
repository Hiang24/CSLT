def nhap():
    print('Nhap 3 so nguyen:')
    a= int(input('a='))
    b= int(input('b='))
    c= int(input('c='))
    return a,b,c
def max3(a,b,c):
    kq=max(a,b,c)
    return f'So lon nhat la: {kq}'
def inkq(kq):
    print(max3(a,b,c))
a,b,c=nhap()
kq=max3(a,b,c)
inkq(kq)