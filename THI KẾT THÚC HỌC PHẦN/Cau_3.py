chuoi = input().split()
K = []
for i in chuoi:
    if i not in K:
        K.append(i)
dem = len(K)
print(dem)