import math
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
p=(a+b+c)/2
s=round(math.sqrt(p*(p-a)*(p-b)*(p-c)),3)
if (a+b)>c and (a+c)>b and (b+c)>a:
    print("Dien tich=",s,sep="")
else:
    print("Khong hop le")