n = int(input('n = '))
if n % 3 == 0 and n % 5 != 0:
    print('Pizz')
elif n % 3 != 0 and n % 5 == 0:
    print('Buzz')
elif n % 3 == 0 and n % 5 == 0:
    print('PizzBuzz')
else:
    print(n)