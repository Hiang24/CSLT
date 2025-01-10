n=int(input())
if 0<=n<=9999:
    for i in str(n):
        if i=='0':
            print('A',end='')
        elif i=='1':
            print('B',end='')
        elif i=='2':
            print('C',end='')
        elif i=='3':
            print('D',end='')
        elif i=='4':
            print('E',end='')
        elif i=='5':
            print('F',end='')
        elif i=='6':
            print('G',end='')
        elif i=='7':
            print('H',end='')
        elif i=='8':
            print('K',end='')
        else:
            print('L',end='')