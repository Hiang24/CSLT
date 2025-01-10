def LaSoNguyenTo(a):
    for i in range (2,a):
        if  a % i == 0:
            return False
    return True
    
def SoHopLe(a):
    if a > 1:
        return False
    if a <= 1 :
        return 1
        
def NhapVaDem():
    flag =  True
    dem = 0
    print('nhap: ')
    while(flag == True):
        inp = int(input())
        if(SoHopLe(inp)==False and LaSoNguyenTo(inp) == True):
            dem = dem +1
        if(SoHopLe(inp)==True):
            flag = False
    return dem
def InKq(dem):     
  print(f'Co {dem} so nguyen to.')    
dem=NhapVaDem()
InKq(dem)