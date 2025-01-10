n=int(input('n='))
if n>=2 and n<=100:
    for i in range(2,n):
        if n%i==0:
            print(n,'khong la SNT')
            break #đèn đỏ
    else:
        print(n,'la SNT')
#Ví dụ nhập số n=50, chạy i từ 2 cho đến 50, khi chạy đến số i=5 thì 50 chia hết cho 5 tức là n chia hết cho i
#thì dừng và in ra là n không phải là số nguyên tố         