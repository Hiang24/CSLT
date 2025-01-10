n=int(input('n='))
L=[]
M=[]
for i in range(0,n):
    x=int(input())
    L.append(x)
for i in L:
    if i not in M: #kiểm tra xem phần tử i có trong danh sách M hay không
        M.append(i) #Nếu không có, tức là phần tử i là mới, thì thực hiện thêm phần tử i
for x in M:
    print(x,end=' ')