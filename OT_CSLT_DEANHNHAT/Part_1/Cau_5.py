n = int(input('n = '))
arr = []
result = []
tong_arr = 0
print('arr =')
for i in range(n):
    x = int(input())
    arr.append(x)
    tong_arr += x
for j in range(len(arr)):
    tong_result = tong_arr
    tong_list = tong_result - arr[j]
    result.append(tong_list)
print(f'arr = {arr}')
print(f'result = {result}')