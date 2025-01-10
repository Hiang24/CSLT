eln=input()
kitu = ['$','#','@']
do_dai = False
in_hoa = False
in_thuong = False
so = False
ki_tu_db = False
khoang_trang = False
if len(eln)>=6 and len(eln)<=17:
    do_dai = True
for i in eln:
    if i.isupper():
        in_hoa = True
    if i.islower():
        in_thuong = True
    if i.isnumeric():
        so = True
    if i in kitu:
        ki_tu_db = True
    if " " not in eln:
        khoang_trang = True
if do_dai == True and in_hoa == True and in_thuong == True and so == True and ki_tu_db == True and khoang_trang == True:
    print(True)
else:
    print(False)