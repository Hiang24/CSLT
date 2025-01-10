n = input()
num = int(input())
L = n.split()
M = []
for i in L:
    so = int(i)
    M.append(so)
for i in range(len(M)):
    if M[i] == num:
        print(i+1)
if num not in M:
    print(0)