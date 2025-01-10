numbers = []  # Danh sách để lưu trữ các số
while True:
    number = input()
    if number == "Q":
        break  # Kết thúc vòng lặp khi nhập Q    
    try:
        number = float(number)  # Chuyển đổi số từ chuỗi thành số thực    
        if number.is_integer() and number > 0:
            numbers.append(int(number))  # Lưu trữ số nguyên dương vào danh sách            
    except ValueError:
        pass  # Bỏ qua nếu không thể chuyển đổi thành số thực
total = sum(numbers)  # Tính tổng các số nguyên dương
print(total)

