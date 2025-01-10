def int2hex(n):
    HEX=[0,1,2,3,4,5,6,7,8,9,'A', 'B', 'C' ,'D', 'E' ,'F']
    x=HEX[n]
    print('HEX:',x)

def hex2int(m):
    INT={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    y=INT[m]
    print('DEC:',y)
try:
    m=str.upper(input('Nhập chữ số muốn chuyển sang DEC: '))
    hex2int(m)
    n=int(input('Nhập số muốn chuyển sang HEX: '))
    int2hex(n)
except:
    print('loi')
    