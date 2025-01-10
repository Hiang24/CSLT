str = input()
in_hoa = 0
in_thuong = 0
chu_so = 0
khac = 0
for i in str:
    if i.isupper():
        in_hoa += 1
    elif i.islower():   
        in_thuong += 1
    elif i.isnumeric():
        chu_so += 1
    else:
        khac += 1
print(f'In hoa: {in_hoa}')
print(f'In thuong: {in_thuong}')
print(f'Chu so: {chu_so}') 
print(f'Khac: {khac}')