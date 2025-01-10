a = float(input())
b = float(input())
c = float(input())
dtb = round((a + b + c)/3,2)
print(dtb)
if 10 >= dtb >= 9:
    print('Xuat sac')
elif dtb >= 8:
    print('Gioi')
elif dtb >= 6.5:
    print('Kha')
elif dtb >= 5:
    print('Trung binh')
elif 5 > dtb >= 0:
    print('Yeu')