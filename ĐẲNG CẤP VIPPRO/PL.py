str_1 = input("Nhập chuỗi 1: ")
str_2 = input("Nhập chuỗi 2: ")

str_2_reversed = ""
for i in range(len(str_2)-1, -1, -1):
    str_2_reversed += str_2[i]

position = 0
for i in range(len(str_1)):
    if str_1[i:i+len(str_2_reversed)] == str_2_reversed:
        position = i
        break

print(position)


