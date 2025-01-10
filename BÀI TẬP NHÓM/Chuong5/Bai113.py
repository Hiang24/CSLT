def Input():
    L=[]
    while True:
        ki_tu = input()
        if ki_tu == '':
            break
        else:
            L.append(ki_tu)
    return L
def VanBan(L):
    if len(L)==0:
        return 'Error'
    elif len(L)==1:
        return str(L[0])
    elif len(L)==2:
        return str(L[0]) + ' and ' + str(L[-1])
    else:
        return (', '.join(L[:-1]) + f' and {str(L[-1])}') 
        '''Sử dụng lệnh join để thêm các dấu ',' vào giữa các kí tự có sổ chỉ mục từ 0 đến -1
        tức là từ kí tự ban đầu đến kí tự có số chỉ mục là -2 (cạnh cuối là -1), và trước kí
        tự cuối cùng (số chỉ mục -1) thì cộng với 'and'.'''
L=Input()
ketqua=VanBan(L)
print(VanBan(L))