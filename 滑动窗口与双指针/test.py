dic = {'a': 10, 'b': 20, 'c': 15}

key_max = max(dic, key=dic.get)
value_max = dic[key_max]
print(f'the max key is: {key_max}, the max value is: {value_max}')
