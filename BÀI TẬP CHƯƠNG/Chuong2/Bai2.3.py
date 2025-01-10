import math
print("Nhap hai canh ke cua tam giac vuong:")
a=int(input())
b=int(input())
c=a**2
d=b**2
e=round(math.sqrt(c+d),2)
print("Canh ke thu nhat la: "+str(a)+", canh ke thu hai: "+str(b)+", co canh huyen =",e,)