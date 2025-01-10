s = input('s = ')
lc = [] #lc là viết tắt của list chuỗi
kq = []
for c in s:
    lc.append(c)
for i in range(len(lc)):
    if lc[i].isalpha() and lc[i - 1] != lc[i + 1]:
        kq.append(lc[i])
op = ''.join(kq)
print(op)