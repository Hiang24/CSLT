# Đề sửa lại là nhập mỗi chuỗi kí tự cách nhau bằng khoảng trắng, tìm và in ra kí tự dài và ngắn nhất lưu vào List
arr = input('arr = ').split()
arr.sort(key = len, reverse=True) #Sắp xếp list theo thứ tự giảm dần len
arr_kq = []
arr_kq.append(arr[0])
arr_kq.append(arr[-1])
print(arr_kq)