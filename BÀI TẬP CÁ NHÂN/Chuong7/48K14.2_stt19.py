while True:
    p=input()
    if len(p)<8:
        print('Không hợp lệ')
    elif not any(char.isupper() for char in p):
        print('Không hợp lệ')
    elif not any(char.islower() for char in p):
        print('Không hợp lệ')
    elif not any(char.isdecimal() for char in p):
        print('Không hợp lệ')
    elif not p.isalnum():
        print('Không hợp lệ')
    else:
        print('Hợp lệ')
        break
