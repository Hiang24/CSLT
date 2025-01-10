eln = input()
in_thuong = False
in_hoa = False
so = False
ki_tu_dac_biet = False
KTDB = ['$','#','@']
do_dai = False
khoang_trang = False
if 6 <= len(eln) and len(eln) <= 17:
    do_dai = True
for i in eln:
    if i.islower():
        in_thuong = True
    if i.isupper():
        in_hoa = True
    if i.isnumeric():
        so = True
    if i in KTDB:
        ki_tu_dac_biet = True
    if i != ' ':
        khoang_trang = True
if do_dai == True and in_thuong == True and in_hoa == True and so == True and ki_tu_dac_biet == True and khoang_trang == True:
    print(True)
else:
    print(False)
    