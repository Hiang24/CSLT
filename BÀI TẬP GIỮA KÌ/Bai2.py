#Nhập dãy số nguyên dương, kết thúc bằng số 0
#Khi kế thúc, thực hiện tính tổng các số lẻ trong dãy
le=0
while True:
	n=int(input())
	if n<0:
		continue
	elif n%2!=0:
		le+=n
	elif n==0:
		break
print('Tong cac so le:',le)
