#Nhập input là HV hoặc HCN
#Nếu là HV thì yêu cầu nhập cạnh, HCN thì nhập dài rộng và sau đó tính chu vi
n=input()
if n=='hv':
    a=int(input('a='))
    print('Chu vi:',a*4)
elif n=='hcn':
    a=int(input('a='))
    b=int(input('b='))
    print('Chu vi:',(a+b)*2)
