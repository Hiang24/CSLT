d = {}
while True:
    a = input()
    if a == '':
        break
    else:
        b = a.split()
        d[b[0]] = int(b[1])
for k,v in d.items():
    if v >= 200:
        print(k,end=', ')