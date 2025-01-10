#Cach 1
L=[]
print('Nhay day so:')
while True:
    a=int(input())    
    if a!=0:
        L.append(a)
    else:
        break
n=int(input('n='))
if n in L:
    print(n,'co ton tai')
else:
    print(n,'khong ton tai')


