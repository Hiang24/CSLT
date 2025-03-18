n=int(input('n = '))

A = list(map(int, input().split()))

count_max = 0

if len(A) == n:

    for i in A:
        count = A.count(i)
        if count > count_max:
            count_max = count

    result = []
    for i in A:
        if A.count(i) == count_max and i not in result:
            result.append(i)

    result.sort()

    for i in result:
        print(i,end=' ')