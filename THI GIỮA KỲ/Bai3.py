"""
Đề bài: Tính lương của nhân viên dựa trên các thông số sau:
- Nhập lương cơ bản (≤ 1000)
- Nhập số giờ làm việc (≤ 30000)
- Nhập loại thuế (A, B, C, D, E) với tỷ lệ thuế tương ứng (0%, 10%, 20%, 29%, 35%)
- Nhập có đóng góp (y/n) - nếu có thì cộng thêm 10

Công thức: Lương = Lương cơ bản × Số giờ + Tiền thuế + (10 nếu có đóng góp)
"""

luong = float(input())
sogio = float(input())
thue = input()
donggop = input()
if luong <= 1000 and sogio <= 30000:
    tienthue = 0
    if thue == 'A':
        tienthue= luong * sogio * 0
    elif thue == 'B':
        tienthue = luong * sogio * 0.1
    elif thue=='C':
        tienthue = luong * sogio * 0.2
    elif thue=='D':
        tienthue=luong * sogio * 0.29
    elif thue=='E':
        tienthue = luong * sogio * 0.35
    ketqua = 0
    if donggop == 'y':
        ketqua= luong * sogio + tienthue + 10
        print(round(ketqua,2))
    elif donggop == 'n':
        ketqua = luong * sogio + tienthue
        print(round(ketqua,2))