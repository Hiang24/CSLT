def giaithua(n):
    if n==0 or n==1:
        return 1
    else:
        return n+giaithua(n-1)
    
n=5
ketqua = giaithua(n)
print(ketqua)