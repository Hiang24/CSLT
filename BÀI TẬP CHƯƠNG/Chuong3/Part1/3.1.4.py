t=int(input(""))
l=int(input(""))
h=int(input(""))
dtb=((t*2)+(l*3)+h)/6
if dtb>=9 and dtb<10:
    print("Xuat sac")
elif dtb>=8:
    print("Gioi")
elif dtb>=7:
    print("Kha")
elif dtb>=6:
    print("Trung binh Kha")
elif dtb>=5:
    print("Trung binh")
elif dtb>=3:
    print("Yeu")
else:
    print("Kem")
