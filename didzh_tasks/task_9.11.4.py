import json
s = input()
try:
    number = int(s)
    num_dict = {i: i ** 2 for i in range(1, number + 1)}
    print(json.dumps(num_dict, ensure_ascii=False))
except:
    print("передайте число")


#Другой вариант
# if s.isdigit(): #Проверка на целое число
#     num_dict = {i: i ** 2 for i in range(1, int(s) + 1)}
#     print(json.dumps(num_dict, ensure_ascii=False))
# else:
#     print("передайте число")