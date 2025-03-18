def Nhap():
    n = int(input('n = '))
    return n

def LaSNT(i):
    if i < 2:
        return False
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            return False
    return True

def LaSoDep(i):
    N = ["3","5","7"]
    for j in str(i):
        if j in N:
            return False
    return True

def DemSoDep(n):
    dem = 0
    for i in range(2,n + 1):
        if LaSNT(i) and LaSoDep(i):
            dem += 1
    return dem

n = Nhap()
print(DemSoDep(n))