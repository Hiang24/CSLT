chuoi=input()
demchu=0
demso=0
for i in chuoi:
    if i.isalpha():
        demchu+=1
    elif i.isdecimal():
        demso+=1
print(f'Chu cai: {demchu}')
print(f'Chu so: {demso}')