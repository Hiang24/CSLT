while True:
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
    l=input('Tiep tuc:')
    if l=='T' or l=='t':
        break  
