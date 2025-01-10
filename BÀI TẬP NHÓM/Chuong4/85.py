def Nhap():
    n = int(input("n:"))
    return n

def ordinal(n):
    if 1<=n<=12:
        if n == 1 :
            tt = 'st'
        elif n == 2 :
            tt = 'nd'
        elif n == 3 :
            tt = 'rd'
        else:
            tt = 'th'
        kq = str(n) + tt
    else: kq = None
    return kq
    
def In_ket_qua(kq):
    print("So thu tu:",kq)
    
if __name__ == "__main__": 
    n=Nhap()               
    x = ordinal(n)
