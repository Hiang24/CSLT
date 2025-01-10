# Thay input lại là nhập số cách với nhau bằng 1 khoảng trắng
L = input().split()
N = []
for a in L:
    N.append(int(a))
tong = 0
for b in N:
    dem = 0
    for i in range(1,b+1):
        if b % i == 0:
            dem += 1
    if dem == 2:
        tong += i
print(tong)
    