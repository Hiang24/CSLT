while True:
    a = float(input('a='))
    b = float(input('b='))
    toan_tu = input('Toan tu:')

    if toan_tu == '+':
        result = a + b
        print(f'{a}+{b}={result}')
    elif toan_tu == '-':
        result = a - b
        print(f'{a}-{b}={result}')
    elif toan_tu == '*':
        result = a * b
        print(f'{a}*{b}={result}')
    elif toan_tu == '/':
        if b != 0:
            result = a / b
            print(f'{a}/{b}={result}')
            
    tiep_tuc = input('Tiep tuc:')
    if tiep_tuc == 'T' or tiep_tuc == 't':
        break