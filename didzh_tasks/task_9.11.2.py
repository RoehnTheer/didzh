# Task 9.11.2
import json
string = input().split(" ")
if len(string) % 2 != 0:
    string.pop()
keys = []
values = []
for i in range(len(string)):
    if i % 2 == 0:
        keys.append(string[i])
    else:
        values.append(string[i])
my_dict = dict(zip(keys, values))
print(json.dumps(my_dict, ensure_ascii=False))


# Другой вариант
# import json
# input_values = input().split()
# keys = input_values[::2]
# values = input_values[1::2]
# data = dict(zip(keys, values))
# print(json.dumps(data, ensure_ascii=False))


# Ещё вариант
# s = input().split()
# my_dict = {s[i-1]:s[i] for i in range(1, len(s), 2)}
# print(json.dumps(my_dict, ensure_ascii=False))