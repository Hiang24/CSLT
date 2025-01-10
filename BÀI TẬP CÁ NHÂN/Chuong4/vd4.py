def NhapBanKinh():
    x=int(input("Ban kinh="))
    return x

def TinhChuVi(y):
    PI = 3.14
    ChuVi=y*PI
    return ChuVi

BanKinh=NhapBanKinh()
ChuVi=TinhChuVi(BanKinh)
print('Chu vi hình tròn: ',ChuVi)