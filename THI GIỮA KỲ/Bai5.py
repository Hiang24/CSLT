"""
Đề bài: Nhập vào hai số nguyên a và b (a, b ≥ 0). Tính tổng các số từ a đến b-1.
Ví dụ:
- Input: 
  2
  5
- Output: 9 (vì 2 + 3 + 4 = 9)
"""

a=int(input())
b=int(input())
if a>=0 and b>=0:
    t=0
    for i in range (a,b):
        t+=i
    print(t)