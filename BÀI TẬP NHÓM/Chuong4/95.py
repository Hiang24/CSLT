import random
def BienSo():
    tile = random.randint(0, 1)  # 0: biển số cũ, 1: biển số mới
    chu = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    so = "1234567890"
    if tile==0:
        bienso_chu=random.choices(chu,k=3) # 3 chữ cái in hoa
        bienso_so=random.choices(so,k=3) # 3 chữ số
        ketqua1 = ''.join(bienso_chu + bienso_so)  # nối chữ cái và chữ số lại thành một biển số
        return 'Bien so cu:',ketqua1
    else:
        bienso_chu=random.choices(chu,k=3) # 3 chữ cái in hoa
        bienso_so=random.choices(so,k=4) # 3 chữ số
        ketqua2=''.join(bienso_so + bienso_chu)  # nối chữ cái và chữ số lại thành một biển số
        return 'Bien so moi:',ketqua2
# Test
x,y=BienSo()
print(x,y)  