s = list(map(int,input('s = ').split()))
tong = 0
for n in s:
    tong += n
sln = max(s)
print(f'Tổng điểm: {tong},Số lớn nhất: {sln}')

# CÁCH KHÔNG DÙNG MAP

# s_str = input('s = ').split()
# s_int = []
# for char in s_str:
#     s_int.append(int(char))
# tong = 0
# for n in s_int:
#     tong += n
# sln = max(s_int)
# print(f'Tổng điểm: {tong},Số lớn nhất: {sln}')