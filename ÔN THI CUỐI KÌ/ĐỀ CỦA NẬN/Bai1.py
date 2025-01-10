so_nguyen = []
while True:
    n = input()
    if n == 'Q':
        break
    try:
        n = float(n)
        if n.is_integer() and n > 0:
            so_nguyen.append(int(n))
    except ValueError:
        pass
tong = 0
for i in so_nguyen:
    tong += i
print(tong)