A = input().split()
B = []
for i in A:
    B.append(int(i))
B.sort()
print(f'{B[-1]}\n{B[-2]}\n{B[-3]}')