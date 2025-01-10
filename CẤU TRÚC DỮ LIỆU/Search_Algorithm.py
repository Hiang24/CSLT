def Linear_Search(a,x): # Tìm kiếm tuần tự
    for i in range(len(a)):
        if a[i]==x: return i
    return -1

def Binary_Search(a,x):
    a.sort()
    print(a)
    left =0
    right = len(a)-1
    while left <= right:
        i = int((left+right)/2)
        if x==a[i]: return i
        if x>a[i]: left=i+1
        else: right=i-1
    return -1



arr = [39,48,10,15,7,9]
# print(Linear_Search(arr,14)) # O(n)
print(Binary_Search(arr,8)) #O(log2(n))
