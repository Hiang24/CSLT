# Đầu vào: List có cấu trúc List trong List
input_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Duyệt qua từng phần tử của List trong List
for i in range(len(input_list)):
    for j in range(len(input_list[i])):
        # Kiểm tra nếu phần tử là số chẵn thì thay bằng chuỗi "x"
        if input_list[i][j] % 2 == 0:
            input_list[i][j] = "x"

# In kết quả
print(input_list)
