while True:
    a=(input('a='))
    if a.isdecimal():
        break
    else:
        print('Nhập lại:')
while True:
    b=(input('b='))
    if b.isdecimal():
        break
    else:
        print('Nhập lại:')
print(f'Tổng {a}+{b}={int(a)+int(b)}')