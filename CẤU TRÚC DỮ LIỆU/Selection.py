def SelectionSort(a,n):
    for i in range(0,n-1):
        min = i
        for j in range(i+1,n):
            if (a[j] < a[min]):
                min = j
        if (min != i):
            temp = a[min]
            a[min] = a[i]
            a[i] = temp
    return a
a = [9,5,1,6,4]
n = len(a)
SelectionSort(a,n)
print(a)