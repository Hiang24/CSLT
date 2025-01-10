
duong=0
am=0
while True:
	n=int(input())
	if n>0:
		duong+=1
	elif n<0:
		am+=1
	else:
		break
print(duong,'so duong')
print(am,'so am')