n = input()
L = n.split(',')
M = []
for i in L:
    stp = int(i,2)
    if stp%3 == 0:
        M.append(i)
ketqua = ','.join(M)
print(ketqua)