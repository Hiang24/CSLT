n=int(input('n='))
L=[]
for i in range(n):
    a=int(input())
    L.append(a)
snd = 0
tong = 0
dem_so_chan = 0
for i in L:
    if i > 0:
        snd+=1
    if i % 2 == 0:
        tong+=i
        dem_so_chan+=1
print(f'SND={snd}')
if tong == 0:
    print(f'TBC=0')
else:
    print(f'TBC={tong/dem_so_chan}')