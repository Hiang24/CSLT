while True:
    n = int(input())
    if n < 0:
        break
    elif n == 0:
        print('1')
    else:
        a = 1
        for i in range(1, n+1):
            a *= i
        print(a)
