x = int(input('x = '))
k = int(input('k = '))
choices = []
if x >= 2 and x % 2 == 0:
    print('choices =')
    for i in range(1, k+1):
        c = input()
        if c == 'move' or c == 'jump':
            choices.append(c)
    for a in choices:
        if a == 'move':
            x += 2
        elif a == 'jump':
            x += 4
kq = x - 1        
print(choices)
print(f'Tòa nhà số lẻ: {kq}')