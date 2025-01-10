a=int(input())
b=int(input())
if a>=0 and b>=0:
    t=0
    for i in range (a,b):
        t+=i
    print(t)