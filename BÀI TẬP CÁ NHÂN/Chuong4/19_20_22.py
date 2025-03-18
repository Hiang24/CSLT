# Role: Bua_1; Keo_2; Bao_3
# Người nhập từ 1 đến 3
# Máy chạy ngẫu nhiên từ 1 đến 3
# Cho phép chơi nhiều lần cho đến khi người nhập vào số 0.
# Ba trạng thái: Người thắng; Máy thắng; Hòa
import random
def KBB(nguoi,may):
    if (nguoi==1 and may==2) or (nguoi==2 and may==3) or (nguoi==3 and may==1):
        print('Kết quả: Người thắng')
    elif nguoi==may:
        print('Kết quả: Hòa')
    else:
        print('Kết quá: Máy thắng')
while True:
    nguoi=int(input('Người: '))
    if nguoi<1 or nguoi>3:
        break
    may=random.randint(1,3)
    print('Máy: ',may)
    KBB(nguoi,may)
    tieptuc=int(input('Tiếp tục: '))
    if tieptuc==0:
        break
    
# import random
# def Nguoi():
#     n=int(input("Human:"))  
#     if 0<=n<=3:
#         return n
# def May():
#     m=random.randint(1,3)
#     print("Computer:",m,sep="")
#     return m
# def Xu_xi(n,m):
#     kq=''
#     if n==m:
#         kq="Draww!"
#     elif (n==1 and m==2) or (n==2 and m==3)or(n==3 and m==1):
#         kq="Human Win!"
#     else:
#         kq="Computer Win!"
#     return kq
# def KQ(kq):
#     print("Result:",kq,sep="")
# while True:
#     n=Nguoi()
#     if n==0:
#         break
#     if n!=0:
#         m=May()
#         x=Xu_xi(n,m)
#         KQ(x)