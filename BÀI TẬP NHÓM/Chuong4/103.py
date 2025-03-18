from Bai100 import NhapNgayThang
def ChonNgay(ngay,thang,nam):
    if ngay*thang==nam%100:
        kq=True
        return kq
def MagicDate():
    for nam in range(1901,2000):
        for thang in range(1,13):
            for ngay in range(1,NhapNgayThang(thang,nam)):
                if ChonNgay(ngay,thang,nam):
                    print('Magic Date is: {}/{}/{}'.format(ngay,thang,nam))    
MagicDate()