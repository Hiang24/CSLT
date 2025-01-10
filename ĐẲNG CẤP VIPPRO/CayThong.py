def print_pattern(s):
    n = len(s)
    for i in range(n):
        print(' ' * (n - i - 1) + s[:i + 1])

# Nhập chuỗi từ bàn phím
input_str = input("Nhập chuỗi kí tự: ")

# In ra màn hình theo yêu cầu
print_pattern(input_str)
