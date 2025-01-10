# Viết chương trình sử dụng hàm:
# a. Nhập từ bàn phím hai số nguyên x và n, và n số nguyên lưu trữ vào list L.
# b. Tìm tất cả các số nguyên đồng thời chia hết cho 2 và 3, thay nó bằng x. In kết quả lên màn hình;
# c. Xóa tất cả các phần tử có giá trị bằng x xuất hiện trong tập trên. In lên màn hình tổng giá trị của các phần tử còn lại.
x = int(input('x='))
def Nhap():
    n = int(input('n='))
    L = []
    for i in range(n):
        a = int(input())
        L.append(a)
    return L
def T_The(x,L):
    for i in range(len(L)):
        if L[i] % 2 == 0 and L[i] % 3 == 0:
            L[i] = x
    for a in L:
        print(a,end=', ')
        print()
    return L
def Tong(x,L):
    s = 0
    while x in L:
        L.remove(x)
    for i in L:
        s += i
        print(i, end=', ')
    print(f'\nSum: {s}')
L = Nhap()
T_The(x,L)
Tong(x,L)