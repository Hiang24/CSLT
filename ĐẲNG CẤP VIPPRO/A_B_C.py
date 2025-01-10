n, m = input().split()
start = ord(n)
end = ord(m)
for i in range(start, end + 1):
    print(chr(i).upper(), end=' ')
