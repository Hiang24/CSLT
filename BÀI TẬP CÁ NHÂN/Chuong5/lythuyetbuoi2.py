'''chuc nang xoa phan tu trong list co 3 cach
del(L[i])-phai dung index
L.remove(x)-xoa phan tu dau tien tim thay
L.pop(i)-xoa phan tu co so chi muc i va tra ve gia tri cua pt do 
'''
#Phuong thuc method
mypet=['zophie','pooka','fat-tail']
#phuong thuc index()-Tra ve in dex cua mot phan tu tim thay trong list
mypet=['zophie','pooka','fat-tail']
namepet='zophie'
if namepet in mypet:
    print('so chi muc la',mypet.index(namepet))
else:
    print('khong ton tai')
    #xoa cac phan tu
L=[1,2,3,4,5,6,4]
x=4
i=0
while i<len(L):    
    if x in L:
        del(L[L.index(x)])
    i+=1
print(L)
#phuong thuc append(x)-Them phan tu x vao cuoi List
L=[1,2,3,4,5,6,4]
x=int(input('x='))
L.append(x)
print(L)
#phuong thuc insert(i,x)-chen` x vao vi tri truoc i hien co trong List;
L=[1,2,3,4,5,6,4]
x=int(input('x='))
L.insert(1,x)
print(L)
#phuong thuc remove()-xoa phan tu x dau tien tim thay trong tap hop
name=['khang','nhu','hung']
name.remove('hung')
print(name)
    #bai xoa phan tu
L=[1,2,3,4,5,6,4]
x=4
i=0
while i<len(L):    
    if x in L:
        L.remove(x)
    i+=1
print(L)
#phuong thuc sort()-cho phep sap xep cac phan tu trong list co thu tu:
    #sort ko co tham so thi` tang dan`
a=[4,5,64,2,9,5]
a.sort()
b=['an','ce','be']
b.sort()
    #sort co them reverse=True thi giam dan
a.sort(reverse=True)
#phuong thuc reverse()-dao nguoc thu tu cac phan tu trong List
c=[1,2,3,4,5]
c.reverse()
#phuong thuc clear()-xoa all cac phan tu trong list
number=[1,2,3,4,5]
number.clear()
#phuong thuc count(x)-thuc hien dem cac phan tu x xuat hien trong List
number1=[1,2,3,4,5]
print(number1.count(3))
    #bai 2
a=[4,5,64,2,9,5]
x=int(input('x='))
if x in a:
    while a.count(x)>0:
        a.remove(x)
print(a)
#phuong thuc pop(i)-Thuc hien xoa va lay ra gia tri cua phan tu co so chi muc i trong list-neu tham so i de trong thi mac dinh la lay phan tu cuoi trong list
v=[1,2,3,4,5]
b=v.pop(2)
print(v,b)
#Phép tham biến
import copy
L1=[1,2,3,4,5]
L2=L1
L2=copy.copy(L1)#tương tự L2=L1.copy()
L1[3]=9
L2[0]=5
print(L1,L2)
'''-add(L,x,k) thêm phần tử x vào list L tại vị trí k
-search(L,x): tìm x trong List L,nếu tìm thấy thì trả về index của x trong L,còn lại trả về None
-delete(L,x): xóa all phần tử có giá trị bằng x trong list L
-count(L):trả về số lượng phần tử trong list L(tương tự hàm len())
-update(L,x,y) tìm x trong List L và thay thế bằng y
'''