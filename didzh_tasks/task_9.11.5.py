import json
my_dict = json.loads(input())
if 'special_key' in my_dict:
    del my_dict['special_key']
print(json.dumps(my_dict, ensure_ascii=False))


# Другой вариант
# import json
# data = json.loads(input())
# data.pop("special_key", True)
# print(json.dumps(data, ensure_ascii=False))