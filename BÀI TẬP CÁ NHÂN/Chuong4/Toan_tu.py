def Nhap():
    a = float(input('a='))
    b = float(input('b='))
    t = input('Toan tu: ')
    return a,b,t
def Toan(a,b,t):
    if t == '+':
        return f'{a} + {b} = {a + b}'
    elif t == '-':
        return f'{a} - {b} = {a - b}'
    elif t == '*':
        return f'{a} * {b} = {a * b}'
    elif t == '/':
        if b != 0:
            return f'{a} / {b} = {a / b}'
        
def InKQ(kq):
    print(Toan(a,b,t))
while True:
    a,b,t = Nhap()
    kq = Toan(a,b,t)
    InKQ(kq)
    chon = input('Tiep tuc: ')
    if chon == 'T' or chon == 't':
        break