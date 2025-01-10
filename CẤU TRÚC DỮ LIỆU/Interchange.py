def InterchangeSort(a,n):
    for i in range(0,n-1):
        for j in range(i+1,n):
            if(a[j]<a[i]):
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    return a
a =[6,8,3,9,1]
n = len(a)
InterchangeSort(a,n)
print(a)