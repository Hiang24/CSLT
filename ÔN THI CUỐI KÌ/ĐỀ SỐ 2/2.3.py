inp = input().split()
chu_so = []
for i in inp:
    if i.isdecimal():
        chu_so.append(int(i))
chu_so.sort()
output = [chu_so[-1],chu_so[0]]
print(output)