# Task 1
# number = float(input().replace(",","."))
# if number > 0:
#     print("Это положительное число")
# elif number < 0:
#     print("Это отрицательное число")
# else:
#     print("Это ноль")


# Task 2
# numbers = input().split(" ")
# num1, num2 = int(numbers[0]), int(numbers[1])
# if num1 > 100 and num2 > 100:
#     if num1 > num2:
#         print(num1)
#     else:
#         print(num2)
# else:
#     print(num2 + 112)


# Task 9.11.1
# import json
# my_dict = json.loads(input())
# for key, value in my_dict.items():
#     if value == min(my_dict.values()):
#         print(key)

# Другой вариант
# import json
# my_dict = json.loads(input())
# print(min(my_dict, key=my_dict.get))

# Task 9.11.2
# import json
# string = input().split(" ")
# if len(string) % 2 != 0:
#     string.pop()
# keys = []
# values = []
# for i in range(len(string)):
#     if i % 2 == 0:
#         keys.append(string[i])
#     else:
#         values.append(string[i])
# my_dict = dict(zip(keys, values))
# print(json.dumps(my_dict, ensure_ascii=False))