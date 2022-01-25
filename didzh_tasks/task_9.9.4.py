import math


weight = input()
if weight.isdigit() == False:
    print("некорректный вес")
    exit()
weight = int(weight)
if weight <= 500:
    print(int(math.ceil(weight/100) * 80))
if 500 < weight <= 1000:
    print(int(math.ceil(weight/100) * 70))
if 1000 < weight <= 10000:
    print(int(math.ceil(weight/100) * 65))
if weight > 10000:
    print("не возим")
