"""
Đề bài: Tính chu vi của hình học
- Nhập vào loại hình ('tg' cho tam giác, 'ht' cho hình tròn)
- Nếu là tam giác: nhập 3 cạnh a, b, c và tính tổng 3 cạnh
- Nếu là hình tròn: nhập bán kính r và tính chu vi (2 × π × r)
- Kết quả làm tròn đến 2 chữ số thập phân

Ví dụ:
- Input: 
  tg
  3
  4
  5
- Output: 12.00

- Input:
  ht
  5
- Output: 31.40
"""

n=input()
Pi=3.14
if n=='tg':
    a=float(input(''))
    b=float(input(''))
    c=float(input(''))
    print(round(a+b+c,2))
elif n=='ht':
    d=int(input(''))
    print(round(d*2*Pi,2))