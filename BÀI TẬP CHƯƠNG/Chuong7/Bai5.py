n = input()
num = int(input())
L = n.split()
M = list(map(int,L)) #Cú pháp chuyển đổi từ list chứa kí tự sang list chứa số
if num in M:
    kq = M.index(num)
    print(kq+1)
else:
    print('0') 
'''map() là một hàm tích hợp sẵn trong Python, được sử dụng để áp dụng một hàm
cho tất cả các phần tử trong một đối tượng lặp lại (như một danh sách, một bộ, 
một chuỗi...) và trả về một iterator chứa kết quả. Cú pháp của hàm map()'''