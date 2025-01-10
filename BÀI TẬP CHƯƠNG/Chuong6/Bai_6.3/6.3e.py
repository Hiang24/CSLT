d = {}
while True:
    a = input()
    if a == '':
        break
    else:
        b = a.split()
        d[b[0]] = int(b[1])
c = input()
for k,v in d.items():
    if k == c:
        dict_tt = {k:v + 100}
d.update(dict_tt)
print(d)