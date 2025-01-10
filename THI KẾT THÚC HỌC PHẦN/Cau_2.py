n=int(input())
dem = 0
for snt in range(1,n+1):
    k = 0
    for i in range(1,snt+1):
        if snt % i == 0:
            k += 1
    if k == 2:
        dem = dem + 1
print(dem)