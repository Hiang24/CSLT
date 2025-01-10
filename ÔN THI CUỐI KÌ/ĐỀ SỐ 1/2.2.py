chuoi_1 = input().split()
chuoi_2 = input().split()
output = []
for i in chuoi_1:
    for j in chuoi_2:
        if i == j:
            output.append(i)
print(output)