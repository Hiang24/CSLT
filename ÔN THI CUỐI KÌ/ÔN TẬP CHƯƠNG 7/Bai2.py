chuoi = input()
ki_tu = chuoi.lower().split()
ki_tu_dau = ki_tu[0]
in_hoa = ki_tu_dau.title()
vanban_new = ' '.join(ki_tu)
output = vanban_new.replace(ki_tu_dau,in_hoa).replace(' , ',', ').replace(' . ','. ').replace(' : ',': ').replace(' ; ','; ')
print(output)