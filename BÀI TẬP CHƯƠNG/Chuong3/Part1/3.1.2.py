a=int(input("M1="))
b=int(input("M2="))
c=int(input("M3="))
s=int(input("S="))
if s<=100:
    print("Phai tra=",(a*s),sep="")
elif s<=150:
    print("Phai tra=",(a*100)+(b*(s-100)),sep="")
else:
    print("Phai tra=",(a*100)+(b*50)+(c*(s-150)),sep="")