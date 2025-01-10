dict1={1: 10, 2: 20, 3: 30}
dict2={4: 40, 5: 50}
dict3={6: 60, 7: 70, 8: 80}
dict_result = {}
for k,v in dict1.items():
    dict_result[k] = v
for k,v in dict2.items():
    dict_result[k] = v
for k,v in dict3.items():
    dict_result[k] = v
print(dict_result)