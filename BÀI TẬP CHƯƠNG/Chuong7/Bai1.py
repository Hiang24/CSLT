chuoi=input()
inhoa = 0
inthuong = 0
chuso = 0
khac = 0
for i in chuoi:
    if i.isupper():
        inhoa += 1
    elif i.islower():
        inthuong += 1
    elif i.isdecimal():
        chuso += 1
    else:
        khac += 1      
print(f'In hoa: {inhoa}')
print(f'In thuong: {inthuong}')
print(f'Chu so: {chuso}')
print(f'Khac: {khac}')