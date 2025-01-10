#tính tổng 3 số cuối ví dụ n=24 => kq=6
n=int(input("n="))
if n==0:
    print(0)
elif n>10 and n<=999:
    a=n//100
    b=n%100
    c=b//10
    d=b%10
    print(a+d+c)