n = int(input())
m = input().split()
x = list(map(int,m))
if n == len(x) and 2<=n<=10**6 and len(x)<=10**9:
    x.sort(reverse=True)
    print(x[1])
else:
    print('NOT FOUND')