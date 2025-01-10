n=int(input())
d=0
a=0
while n!=0:
    if n>0:
        d+=1
        n=int(input())
    else:
        a+=1
        n=int(input())
print(d,'so duong')
print(a,'so am')