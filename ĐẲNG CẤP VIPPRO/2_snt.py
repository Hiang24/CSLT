def Nhap():
    a = int(input())
    b = int(input())
    return a,b
def La_SNT(a,b):
    k = 0
    v = 0
    for i in range(1,a+1):
        if a % i == 0:
            k += 1
    for j in range(1,b+1):
        if b % j == 0:
            v += 1
    if k == 2 and v == 2:
        return True
    else:
        return False
a,b = Nhap()
print(La_SNT(a,b))