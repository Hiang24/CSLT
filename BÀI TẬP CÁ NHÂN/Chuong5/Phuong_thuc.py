names =[1,2,3,4, 5, 6]
names.append(6)
print(names)
names.insert(0,7)
print(names)
names.insert(-2,8)
print(names)
#append(x) thêm phần tử x vào cuối List
#insert(i,x) chèn x vào vị trí i hiện có trong List
n=['A','B','C','D','B']
n.remove('B')
print(n)
#remove(x): xóa phần tử x ĐẦU TIÊN tìm thấy trong List
#sort: sắp xếp các phân tử từ bé đến lớn hoặc a-z (.sort(revese=True)) là sắp xếp giảm dần
numbers1 = [1, 2, 3, 4, 5, 7]
numbers2=numbers1.copy()
print(numbers1)
print(numbers2)
#copy: Tạo bản sao
t = [1, 2, 3, 4, 5]
x=t.pop(4)
print(t)
#print(x)
#pop: thực hiện xóa và lấy ra giá trị của phân tử trong một list