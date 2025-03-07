import math
def nhap():
    print('Nhap 3 so nguyen:')
    a=int(input('a='))
    b=int(input('b='))
    c=int(input('c='))
    return a,b,c
def giaipt(a,b,c):
    if a!=0 and b!=0 and c!=0:
        d=b**2-4*a*c
        if d<0:
            return "Phuong trinh vo nghiem"
        elif d==0:
            x=(-b/2*a)
            return f'Phuong trinh co nghiem kep\nx1=x2={x}'
        else:
            x1=(-b + math.sqrt(d))/(2*a)
            x2=(-b - math.sqrt(d))/(2*a)
            return f'Phuong trinh co hai nghiem\nx1={x1}\nx2={x2}'
def inkq(kq):
    print(giaipt(a,b,c))
      
a,b,c=nhap()
kq=giaipt(a,b,c)
inkq(kq)
