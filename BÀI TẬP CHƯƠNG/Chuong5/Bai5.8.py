A = []
B = []
C = []
m = int(input('m='))
n = int(input('n='))
l = m*n
#Nhập list A với độ dài l
print('A:')
for i in range(0,l):
    #x = int(input())
    #A.append(x)
    A.append(int(input()))
#Nhập list B với độ dài l    
print('B:')
for i in range(0,l):
    B.append(int(input()))
#Tính toán và thêm kết quả vào list C   
for i in range(l):
    C.append(A[i] + B[i])
#In list C theo yêu cầu đề bài
print('C:')
for i in range(0,l):
    print(C[i],end=' ')
    if (i+1) % n == 0:
        print(sep='')
    