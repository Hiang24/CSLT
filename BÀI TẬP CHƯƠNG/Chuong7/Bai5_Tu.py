n=input()
x=int(input())
N=n.split()
u=False
for i in range(len(N)):
    if int(N[i])==x:
        u=True
        print(i+1)
if not u:
    print(0)