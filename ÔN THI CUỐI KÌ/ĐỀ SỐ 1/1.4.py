chuoi = input().split() #Nhập, tách các từ và lưu vào chuỗi
tu = input()
chuoi_new = [] # tạo một chuỗi rỗng
for i in chuoi: #Chạy chuỗi, đầu tên thêm từ ở dòng 2, sau đó thêm từ đầu tiên trong chuỗi, cứ tiếp tục vòng lắp cho đến từ cuối cùng
    chuoi_new.append(tu)
    chuoi_new.append(i)
print(chuoi_new)