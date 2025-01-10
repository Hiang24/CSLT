chuoi = input()
n=int(input())
phan_tich = chuoi.split()
chuoi_so = []
for i in phan_tich:
    so = int(i)
    chuoi_so.append(so)
for j in range(len(chuoi_so)):
    if n == chuoi_so[j]:
        print(j+1)
if n not in chuoi_so:
    print('0')