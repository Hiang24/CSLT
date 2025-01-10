s = input('s = ')
up_count = 0
lo_count = 0
di_count = 0
kq = ''
for a in s:
    if a.isupper():
        up_count += 1
        kq += a.lower()
    elif a.islower():
        lo_count += 1
        kq += a.upper()
    elif a.isdecimal():
        di_count += 1
        kq += '#'
print(f'uppercase_count = {up_count}\nlowercase_count = {lo_count}\ndigit_count = {di_count}\nmodified_sring = {kq}')