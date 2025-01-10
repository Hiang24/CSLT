d = {}
while True:
    a = input()
    if a == '':
        break
    else:
        b = a.split()
        d[b[0]] = int(b[1])
d_copy = d.copy()  
for k,v in d.items():
    if v <= 100:
        del d_copy[k]
print(d_copy)