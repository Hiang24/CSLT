n = int(input())
tong = 0
dem = 0
for i in range(n):
    try:
        x = int(input())
        tong += x
        dem += 1
    except ValueError:
        pass
if dem > 0:
    print(tong/dem)
else:
    print('0')