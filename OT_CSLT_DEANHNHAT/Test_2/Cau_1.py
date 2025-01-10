# Đề thay lại là nhập số nguyên n và nhập n số nguyên nhé
n = int(input('n = '))
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)
arr_le = []
for i in arr:
    if i % 2 != 0:
        arr_le.append(i)
arr_le.sort()
index = 0
for j in range(len(arr)):
    if arr[j] % 2 != 0:
        arr[j] = arr_le[index]
        index += 1
print(arr)
