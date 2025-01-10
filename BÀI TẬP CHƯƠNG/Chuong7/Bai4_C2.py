str = input()
list_tu = str.split(',')
for i in list_tu:
    new_list = list(set(list_tu))
new_list.sort()
ketqua = ','.join(new_list)
print(ketqua)