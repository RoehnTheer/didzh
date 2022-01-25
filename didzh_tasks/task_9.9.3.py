data = input().split()
input_date = [int(x) for x in data if x.isdigit()]
# Вместо всего этого можно было ловить исключение
if ''.join(data).isdigit() == False or len(input_date) != 2 or input_date[0] > 12 \
        or input_date[1] > 31 or input_date[0] == 2 and input_date[1] > 29 \
        or input_date[0] in (4, 6, 9, 11) and input_date[1] > 30:
    print("некорректная дата")
    exit()

zodiac_signs = {"Козерог": [(12, 22), (1, 19)],
                "Водолей": [(1, 20), (2, 18)],
                "Рыбы": [(2, 19), (3, 20)],
                "Овен": [(3, 21), (4, 19)],
                "Телец": [(4, 20), (5, 20)],
                "Близнецы": [(5, 21), (6, 20)],
                "Рак": [(6, 21), (7, 22)],
                "Лев": [(7, 23), (8, 22)],
                "Дева": [(8, 23), (9, 22)],
                "Весы": [(9, 23), (10, 22)],
                "Скорпион": [(10, 23), (11, 21)],
                "Стрелец": [(11, 22), (12, 21)]}

for zodiac, date in zodiac_signs.items():
    if input_date[0] == date[0][0] and input_date[1] >= date[0][1] \
            or input_date[0] == date[1][0] and input_date[1] <= date[1][1]:
        print(zodiac)
