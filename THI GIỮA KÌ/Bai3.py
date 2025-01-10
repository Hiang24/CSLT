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