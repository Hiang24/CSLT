chuoi=input().split()

L=[]
for i in chuoi:
    if i not in L:
        L.append(i)
dem=len(L)
print(dem)