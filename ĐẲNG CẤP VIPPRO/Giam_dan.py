n = int(input())
m = input().split()
x = list(map(int,m))
if n == len(x) and n<=10**4 and len(x)<=10**6:
    x.sort(reverse=True)
for i in x:
    print(i,end=' ')