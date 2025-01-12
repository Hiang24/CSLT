gia_niem_yet = int(input('Nhap gia niem yet: '))
chiet_khau = int(input('Nhap chiet khau: '))

vat = (gia_niem_yet - chiet_khau)*0.01
gia_ban = gia_niem_yet - chiet_khau + vat

print(f'Gia ban: {gia_ban}')