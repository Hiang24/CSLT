def Nhap():
    n = int(input('n='))
    return n
def Dem_SNT(n):
    k = 0
    for snt in range(2,100): #Nếu nộp vẫn sai thì để lên 1000
        dem = 0
        for i in range(1,snt+1):
            if snt % i == 0:
                dem += 1
        if dem == 2:
            k += 1
            print(snt, end=', ')
        if k == n:
            break  #Gox tienegs vieetj khoong duowdjc?????    
n = Nhap()
Dem_SNT(n)
print('à giờ mới gõ được')