"""
Đề bài: Nhập vào số nguyên n (1 ≤ n ≤ 50). In ra n số nguyên tố đầu tiên, các số cách nhau bởi dấu phẩy và khoảng trắng.
Ví dụ:
- Input: 5
- Output: 2, 3, 5, 7, 11
"""

n=int(input())
dem = 0 #Đếm số nguyên tố
if 1<=n<=50: #Chọn vùng của số n
    for snt in range(1,1000): #line 4 đến 11: lệnh kiểm tra số nguyên tố
        k=0 #đếm số lần chia hết
        for i in range(1,snt+1):            
            if snt%i==0:
                k+=1                 
        if k==2:
            dem+=1
            print(snt,end=', ')
        if dem==n: #Khi chọn được 1 snt rồi in ra, thì dem sẽ tăng lên 1, tăng cho đến khi bằng đúng với số n thì dừng
            break    