chuoi = input().split()
tong = 0
list_tong = []
for i in range(len(chuoi)):
    tong += int(chuoi[i])
    list_tong.append(tong)
for a in list_tong:
    print(int(a),end= ' ')
