def InsertionSort(a):
    for i in range(len(a)-1): #O(n)
        x = a[i+1]
        pos = i
        while pos>=0 and a[pos]>x: #O(n)
            a[pos+1]=a[pos]
            pos-=1
        a[pos+1]=x
    return a
a = [3,5,7,4,1,6]
InsertionSort(a)
print(a)