N = list(map(int,input().split()))
tong = 0
dem_chan = 0
nguyen_duong = None
for i in N:
    tong += i
    if i % 2 == 0:
        dem_chan += 1
for j in range(len(N)):
    if N[j] > 0:
        nguyen_duong = N[j]
if nguyen_duong is not None:
    print(tong, dem_chan, nguyen_duong, end=' ')
else:
    print(tong, dem_chan, 0, end=' ')
