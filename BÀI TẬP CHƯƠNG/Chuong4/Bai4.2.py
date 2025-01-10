def nhap():
    n=int(input("n="))
    return n
def inkq(n):
    for a in range(2,n+1,2):
        print(a,end=" ")
    print()
while True:       
    n=nhap()
    inkq(n)
    chon = str(input("Tiep tuc khong?"))
    if chon == 'k' or chon =='K':
        break