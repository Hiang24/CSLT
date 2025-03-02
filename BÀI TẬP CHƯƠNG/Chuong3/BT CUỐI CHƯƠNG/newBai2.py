n = int(input('n = '))
if 1 <= n <= 100:
    k = 0
    for i in range(1,n+1):
        if n % i == 0:
            k += 1
    if k == 2:
        print(f'{n} là số nguyên tố')
    else:
        print(f'{n} không là số nguyên tố')