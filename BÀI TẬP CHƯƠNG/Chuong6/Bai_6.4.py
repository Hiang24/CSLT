n = int(input())
L_str = []
L_int = []
d = {}
for i in range(n):
    a = input()
    L_str.append(a)
for j in range(n):
    b = int(input())
    L_int.append(b)
for x in range(n):
    d[L_str[x]] = L_int[x]
#Câu a:
print(f'{L_str}\n{L_int}\n{d}')
#Câu b:
L_int.sort()
d_sorted ={}
for z in L_int:
    for k,v in d.items():
        if z == v:
            d_sorted[k] = v
print(d_sorted)
#Câu c:
d_copy = d.copy()
inp = input()
inp_int = int(input())
for k,v in d_copy.items():
    if k == inp:
        dict_tt = {k:v + inp_int}
d_copy.update(dict_tt)
print(d_copy)
#Câu d:
d_copy2 = d.copy()
tong = 0
for y in d.values():
    