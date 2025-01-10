import copy
numbers1 = [1,2,3,4,5]
numbers2 = copy.copy(numbers1)
print(numbers2)
numbers3 = numbers1
numbers3[2] =6
print(numbers3)