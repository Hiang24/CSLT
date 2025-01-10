def BubbleSort(a,n):
    for i in range(0,n-1):
        for j in range(n-1,i,-1):
            if a[j] < a[j-1]:
                temp = a[j]
                a[j] = a[j-1]
                a[j-1] = temp
    return a
a =[6,8,3,9,1]
n = len(a)
BubbleSort(a,n)
print(a)