def NhapNgayThang(thang, nam):
    if nam%400==0 or nam%4==0:
        nam_nhuan=True
    elif nam%100==0:
        nam_nhuan=False
    else:
        nam_nhuan=False
    ngay_31=[1,3,5,7,8,10,12]
    ngay_30=[4,6,9,11]
    if nam_nhuan==True and thang==2:
        return 29
    elif nam_nhuan==False and thang==2:
        return 28
    elif thang in ngay_31:
        return 31
    elif thang in ngay_30:
        return 30

    
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