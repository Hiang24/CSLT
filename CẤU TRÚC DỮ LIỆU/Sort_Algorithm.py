def Swap(a,b):
    temp =a
    a=b
    b=temp
    return a,b

#Hoán đổi vị trí cặp nghịch thuật khi trong O(n^2)
# // So sánh các phần tử để đặt các phần tử nhỏ nhất vào vị trí phía trước
def Interchange_Sort(a):
    for i in range(len(a)-1): #O(n)
        for j in range(i+1,len(a)): #O(n)
            if a[i]>a[j]: 
                a[i],a[j]=Swap(a[i],a[j]) 
    return a

#Xác định vị trí index min trong O(n) và hoán đổi trong O(n)
# //so sánh các phần tử để đặt các phần tử nhỏ nhất vào vị trí phía trước
def Selection_Sort(a):
    for i in range(len(a)-1): #O(n)
        Min = i
        for j in range(i+1,len(a)): #O(n)
            if a[j] < a[Min]: Min=j
        if Min!=i: # Giảm số lần hoán vị
            a[i],a[Min]=Swap(a[i],a[Min])
    return a

# Gán x = giá trị tiếp theo trong O(n)
# pos là con trỏ để di chuyển dãy thêm 1 đơn vị 
# nếu giá trị tại pos lớn hơn x  trong O(n)
# // so sánh các phần tử để quyết định vị trí của một phần tử trong mảng đã được sắp xếp một phần
def Insertion_Sort(a):
    for i in range(len(a)-1): #O(n)
        x = a[i+1]
        pos = i
        while pos>=0 and a[pos]>x: #O(n)
            a[pos+1]=a[pos]
            pos-=1
        a[pos+1]=x
    return a

# Hoán đổi các nghịch thuật cặp xếp kề nhau trong O(n) đi từ cuối mảng
# // so sánh các phần tử để đặt các phần tử lớn nhất vào vị trí cuối cùng
def Bubble_Sort(a):
    for i in range(len(a)-1): #O(n)
        for j in range(len(a)-1,i,-1): #O(n)
            if a[j]<a[j-1]: a[j],a[j-1] = Swap(a[j],a[j-1])
    return a

# so sánh các phần tử của phân vùng mảng chưa được sắp xếp 
# thành hai nửa khác nhau xung quanh giá trị pivot
def Quick_Sort(a,left,right):
    if left>=right: return a
    i =left
    j=right
    pivot = a[int((i+j)/2)]
    while i<=j:
        while a[i]<pivot: i+=1
        while a[j]>pivot: j-=1
        if i<=j:
            a[i],a[j] = Swap(a[i],a[j])
            i+=1
            j-=1
    if j>left: Quick_Sort(a,left,j)
    if i<right: Quick_Sort(a,i,right)
    return a

#so sánh các phần tử của hai phần tử đã sắp xếp để hợp nhất chúng thành mảng được sắp xếp cuối cùng
def Merge_Sort(a,left,right): # Chia để lấy index l,m,r của các tập hợp con có nhiều nhất 2 phần tử
    if left>=right: return a
    mid = int((left+right)/2)
    Merge_Sort(a,left,mid)
    Merge_Sort(a,mid+1,right)
    Merge(a,left,mid,right)
    return a

def Merge(a,left,mid,right): # Thực hiện sắp xếp các phần tử theo đúng thứ tự
    i = left
    j = mid+1
    n = int(right-left+1)
    B = [0]*(n)
    k=0
    while i< mid+1  and j< right+1: # thực hiện thêm phần tử vào B theo thứ tự
        if a[i]<a[j]:
            B[k]=a[i]
            k+=1
            i+=1
        else:
            B[k]=a[j]
            k+=1
            j+=1
    while i< mid+1: # Nếu đã tăng j ở trên thì thực hiện tăng i
        B[k]=a[i]
        k+=1
        i+=1
    while j < right+1: # Nếu đã tăng i ở trên thì thực hiện tăng j
        B[k]=a[j]
        k+=1
        j+=1
    i=left
    for k in range(n): # Gán lại các phần tử trong B vào vị trí tương ứng trong A
        a[i]=B[k]
        k+=1
        i+=1
    return a

    
    
arr = [39,48,10,15,7,9]
# print(Interchange_Sort(arr)) #O(n^2)
# print(Selection_Sort(arr)) #O(n^2)
# print(Insertion_Sort(arr)) #O(n^2)
# print(Bubble_Sort(arr)) #O(n^2)
# print(Quick_Sort(arr,0,len(arr)-1)) #O(nlogn)
print(Merge_Sort(arr,0,len(arr)-1)) #O(nlog2(n))
