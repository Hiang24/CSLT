n = int(input('N = '))
tong = 0
for i in range(1,n+1):
    x = int(input(f'Nhập số thứ {i}: '))
 
    if x >= 0:
        tong += x 
           
    if x != 0:
        continue
    elif x == 0:
        break

print(tong)