n = int(input())
m = input().split()
x = list(map(int,m))
L=[]
KQ=[]
if n == len(x) and n<=10**4 and len(x)<=10**8:
    for i in x:
        dem = 0
        for j in range(1,i+1):
            if i%j == 0:
                dem += 1
        if dem == 2:
            L.append(i)
    L.sort()
for i in L:
    if i not in KQ:
        KQ.append(i)
for a in KQ:
    print(a,end=' ')