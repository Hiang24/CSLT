mat_hang = {}
while True:
    ten = input('Nhap ten mat hang: ')
    if ten == "":
        break
    sl = int(input('Nhap so luong: '))
    mat_hang[ten] = sl
print(mat_hang)

# In lên màn hình mặt hàng có số lượng lớn nhất và bé nhất
min_sl = min(mat_hang, key = mat_hang.get) #Cú pháp nên đừng thắc mắc
max_sl = max(mat_hang, key = mat_hang.get)
print(f'Mat hang co so luong nhieu nhat: {max_sl}\nMat hang co so luong it nhat: {min_sl}')

# Sắp xếp tăng dần theo tên
sort_mh = dict(sorted(mat_hang.items()))
print(f'Danh sach sau khi sap xep: {sort_mh}')

# Xóa mặt hàng có số lượng bé hơn 10
for k,v in sort_mh.items():
    if v <= 10:
        del(mat_hang[k])
print(f'Danh sach sau khi xoa: {mat_hang}')

# Tìm hàng
name = input('Nhap ten mat hang: ')
if name in mat_hang.keys():
    print(f'So luong hien tai: {mat_hang[name]}')
else:
    print('Đéo có. Cút!')