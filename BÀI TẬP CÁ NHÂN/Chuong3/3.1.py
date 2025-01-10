a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
max = a
min=b
if b > max:
    max=b
elif c> max:
    max=c
print("SLN=",max,sep=(""))
if a<b:min=a
elif c<min:min=c
print("SBN=",min,sep=(""))