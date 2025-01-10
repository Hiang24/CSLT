x=float(input("x="))
y=float(input("y="))
ch=(input("Phep toan:"))
if ch=="+":
    print("{}+{}={}".format(x,y,round(x+y,1)))
elif ch=="-":
    print("{}-{}={}".format(x,y,round(x-y,1)))
elif ch=="*":
    print("{}*{}={}".format(x,y,round(x*y,1)))
elif ch=="/":
    if y!=0:
        print("{}/{}={}".format(x,y,round(x/y,1)))
    else:
        print("Khong hop le")
else:
    print("Khong hop le")