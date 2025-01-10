str = input()
list_tu = str.split(',')
new_list = []
for i in list_tu:
    if i not in new_list:
        new_list.append(i)
new_list.sort()
ketqua = ','.join(new_list)
print(ketqua)