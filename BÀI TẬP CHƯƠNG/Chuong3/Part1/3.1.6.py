a=float(input())
b=float(input())
c=float(input())
if not (a+b)>c or not (a+c)>b or not (b+c)>a or not a>0 or not b>0 or not c>0:
    print("Khong hop le")
elif a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
    print("Tam giac vuong")
elif a==b and b==c and a==c:
    print("Tam giac deu")
else:
    print("Tam giac loai khac")