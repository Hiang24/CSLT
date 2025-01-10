ht=input("Ho ten: ")
snc=int(input("So ngay cong: "))
dgnc=int(input("Don gia ngay cong: "))
hspc=float(input("He so phu cap: "))
tu=int(input("Tam ung: "))
luong=dgnc*snc*hspc
tl=luong-tu
print("Nhan vien {}, Co tien Luong={}, Tam ung={} va Thuc linh={}".format(ht,luong,tu,tl))