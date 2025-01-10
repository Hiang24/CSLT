d = {}
while True:
    a = input()
    if a == '':
        break
    else:
        b = a.split()
        d[b[0]] = int(b[1])
tong = 0
for i in d.values():
    tong += i
print(tong)