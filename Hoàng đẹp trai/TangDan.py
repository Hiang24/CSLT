n = int(input('n = '))
A = list(map(int, input().split()))

count_dict = {}
for num in A:
    count_dict[num] = count_dict.get(num, 0) + 1

max_count = max(count_dict.values())
result = [num for num, count in count_dict.items() if count == max_count]

result.sort()
print(*result)
