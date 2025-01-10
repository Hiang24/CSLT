# Nhập chuỗi từ người dùng
s = input("Nhập chuỗi: ")

# Khởi tạo biến đếm
count_alpha = 0  # Đếm số chữ cái
count_digit = 0  # Đếm số chữ số

# Duyệt qua từng kí tự trong chuỗi và tăng giá trị đếm tương ứng
for c in s:
    if c.isalpha():
        count_alpha += 1
    elif c.isdigit():
        count_digit += 1

# In kết quả
print("Chu cai:", count_alpha)
print("Chu so:", count_digit)
