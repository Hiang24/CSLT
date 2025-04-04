"""
Đề bài: Nhập vào số nguyên n (0 ≤ n ≤ 10^6). In ra tất cả các số từ 1 đến n mà chia hết cho 3 nhưng không chia hết cho 5.
Ví dụ:
- Input: 20
- Output: 3 6 9 12 18
"""

n=int(input())
if 0<=n<=10**6:
    for i in range(1,n+1):
        if i%3==0 and i%5!=0:
            print(i,end=' ')