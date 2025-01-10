# Đề sửa lại là nhập các câu, mỗi câu cách nhau bằng dấu phẩy và lưu vào 1 list, với keyword, cũng tương tự
L = input('Sentences: ').split()
K = input('Keywword: ').split(',')
for i in range(len(L)):
    for name in K:
        L[i] = L[i].replace(name,"REDACTED")
print(L)