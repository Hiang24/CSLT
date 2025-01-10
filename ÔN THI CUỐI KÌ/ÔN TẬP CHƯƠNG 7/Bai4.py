chuoi = input()
list = chuoi.split(',')
new_list = []
for i in list:
    if i not in new_list:
        new_list.append(i)
new_list.sort()
output = ','.join(new_list)
print(output)