L=[]
n=int(input('n='))
if n>0:
    for j in range(n):
        x=int(input())
        L.append(x)
    M=list(set(L)) #Hàm tự động lấy ra những kí tự trùng nhau và chuyển vào list M
    for x in M:
        print(x,end=' ')
'''set() là một kiểu dữ liệu trong Python giống như list hoặc tuple,
nhưng nó chỉ chứa các phần tử độc nhất. Nó được sử dụng để lưu trữ tập
hợp các phần tử, với tính chất là không có phần tử trùng lặp trong tập hợp.'''