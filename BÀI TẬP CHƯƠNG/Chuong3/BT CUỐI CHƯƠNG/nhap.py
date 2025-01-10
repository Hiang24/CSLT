while True:
    # Nhập hai số thực và toán tử
    a = float(input("Nhập số thực a: "))
    b = float(input("Nhập số thực b: "))
    operator = input("Nhập toán tử (+,-,*,/): ")

    # Tính toán và in kết quả tương ứng
    if operator == '+':
        print(f"{a} + {b} = {a + b}")
    elif operator == '-':
        print(f"{a} - {b} = {a - b}")
    elif operator == '*':
        print(f"{a} * {b} = {a * b}")
    elif operator == '/':
        print(f"{a} / {b} = {a / b}")
    else:
        print("Toán tử không hợp lệ")

    # Hỏi người dùng có muốn tiếp tục hay không
    choice = input("Bạn có muốn tiếp tục không? (T/t để thoát): ")
    if choice == 'T' or choice == 't':
        break