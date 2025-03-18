import math

# Hàm tính khoảng cách giữa hai điểm
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Khởi tạo biến lưu chu vi và điểm đầu tiên
perimeter = 0
first_point = None
last_point = None

while True:
    # Nhập tọa độ x và y từ người dùng
    x = input("Enter the x part of the coordinate: ")
    
    # Kiểm tra nếu người dùng nhập dòng trống để kết thúc
    if x.strip() == "":
        if first_point and last_point:
            # Tính khoảng cách từ điểm cuối cùng về điểm đầu tiên
            x1, y1 = last_point
            x2, y2 = first_point
            perimeter += calculate_distance(x1, y1, x2, y2)
        break
    
    # Nhập giá trị y tương ứng
    y = float(input("Enter the y part of the coordinate: "))
    
    # Chuyển đổi tọa độ x từ chuỗi sang float
    x = float(x)
    
    # Lưu điểm đầu tiên nếu chưa có
    if first_point is None:
        first_point = (x, y)
    
    # Nếu đã có điểm trước đó, tính khoảng cách từ điểm trước đến điểm hiện tại
    if last_point is not None:
        x1, y1 = last_point
        x2, y2 = x, y
        perimeter += calculate_distance(x1, y1, x2, y2)
    
    # Cập nhật điểm cuối cùng
    last_point = (x, y)

# Hiển thị tổng chu vi
print(f"The perimeter of that polygon is {perimeter}")
