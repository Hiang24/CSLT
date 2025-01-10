# Thay đề lại là nhập các số nguyên cách nhau bởi dấu cách
n = input().split()
kq = []
for a in n:
    tong = 0
    for b in a:
        tong += int(b)
        k = 0
        for i in range(1, tong + 1):
            if tong % i == 0:
                k += 1
        if k == 2:
            kq.append(a)
if len(kq) == 0:
    print(-1)
else:
    kq.sort()
    print(kq[-1])
