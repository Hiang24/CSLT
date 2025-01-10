n=int(input('n='))
if 2<=n<=10**6:
    for snt in range(n,1,-1):#chạy từ n về 2 (chạy ngược) vd:chạy từ 10 về 2
        k=0 #k:số lần chia hết
        for i in range(1,snt+1):#Kiểm tra tính chia hết, i:phép thử và chạy từ 1 cho đến snt
            if snt%i==0: #thực hiện phép thử
                k+=1 #Cứ một lần chia hết thì k cộng thêm 1, vd: nếu là 8 thì k=4, nếu là 10 thì k=4
        if k==2: #VÌ snt chỉ chia hết cho 1 và chính nó nên khi và chỉ khi k=2 thì đó là snt
            print('Số nguyên tố gần n nhất:',snt)
            break #khi tìm được snt, dừng chương trình