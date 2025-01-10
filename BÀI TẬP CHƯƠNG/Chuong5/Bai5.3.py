L=[]
u=0
t=0
m=0
n=int(input('n='))
for i in range(1,n+1):
    L+=[int(input())]
for i in L:
    if i>0:
        u+=1
    if i%2==0: 
        t+=i
        m+=1
print('SND=',u)
if m==0:
    print('TBC=0') 
else:
    print('TBC=',t/m)