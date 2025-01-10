dict1={"data1": 5, "data2": 10, "data3": 15}
dict2={"data4": 20, "data5": 25}
dict_tong = {**dict1, **dict2}
tong = 0
for i in dict_tong.values():
    tong += i
print(f'Tong: {tong}')