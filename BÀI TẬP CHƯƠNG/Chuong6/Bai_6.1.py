chuoi = input()
output = {}
list_chuoi = chuoi.split()
for a in list_chuoi:
    if a not in output:
        output[a] = 1
    else:
        output[a] += 1
print(output)