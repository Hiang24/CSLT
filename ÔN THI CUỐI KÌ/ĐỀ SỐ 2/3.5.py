chuoi = input().split()
output = []
for i in chuoi:
    if i not in output:
        output.append(i)
for j in output:
    print(j,end=' ')