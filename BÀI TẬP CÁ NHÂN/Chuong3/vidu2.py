S=0
n=int(input("Nhap n="))
for i in range(1,n+1):
    print("So thu ",i,": ",sep="",end="")
    x=int(input())
    if x<0:
        continue
    elif x==0:
        break
    else:
        S+=x
print("S=",S,sep="")
#Nhập số n, tiếp tục nhập n số nguyên, tính tổng tất cả các số, nếu nhập 0 thì dừng vòng lặp và in ra kết quả