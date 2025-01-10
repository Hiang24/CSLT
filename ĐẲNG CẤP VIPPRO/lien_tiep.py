n = input()
L = []
for a in n:
    L.append(a)
L.sort()
n_sort = ''.join(L)
if int(n) == int(n_sort):
    print('So tang dan deu')
else:
    print('So khong tang dan deu')