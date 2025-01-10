kho = {}
mat_hang = {}
n = int(input('Nhap so luong mat hang: '))
for i in range(n):
    mat_hang['ma_hang'] = int(input('Nhap ma hang hoa: '))
    mat_hang['ten_hang'] = input('Nhap ten hang: ')
    mat_hang['so_luong'] = int(input('Nhap so luong: '))
    mat_hang['ngay_nhap'] = input('Nhap ngay nhap: ')
    mat_hang['ten_nguoi_nhap'] = input('Ten nguoi nhap: ')
    kho[i] = dict(mat_hang)
print(kho)