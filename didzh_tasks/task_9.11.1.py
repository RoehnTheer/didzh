# Task 9.11.1
import json
my_dict = json.loads(input())
for key, value in my_dict.items():
    if value == min(my_dict.values()):
        print(key)

# Другой вариант
# import json
# my_dict = json.loads(input())
# print(min(my_dict, key=my_dict.get))