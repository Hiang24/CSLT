d = {}
while True:
    a = input()
    if a == '':
        break
    else:
        b = a.split()
        d[b[0]] = int(b[1])
print(d)