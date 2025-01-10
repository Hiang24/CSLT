a = input().split()
b = list(map(int,input().split()))
d = {}
if len(a) == len(b):
    for i in range(len(a)):
        d[a[i]] = b[i]
    print(d)
