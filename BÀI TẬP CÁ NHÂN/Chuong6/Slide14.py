sv = {}
n = int(input('Nhap so sinh vien: '))
for i in range(n):
    sv[i] = dict(ma_sv = int(input('Nhap ma sinh vien: ')),
                 ten_mh = input('Nhap ten mon hoc: '),
                 diem_thi = int(input('Nhap diem thi: ')))
nhap = int(input('Ma sinh vien: '))
if nhap == (sv[i]['ma_sv']):
    # print(f'{sv[i]['ma_sv']} {sv[i]['ten_mh']} {sv[i]['diem_thi']}')
    for x in sv[i].values():
        print(x, end=' ')