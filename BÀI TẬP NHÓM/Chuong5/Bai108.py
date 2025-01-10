Am = []
Zero = []
Duong = []
while True:
    num = input()
    if num == '':
        break
    else:
        if int(num)<0:
            Am.append(num)
        elif int(num)==0:
            Zero.append(num)
        elif int(num)>0:
            Duong.append(num)
L= Am + Zero + Duong
for i in L:
    print(i)
