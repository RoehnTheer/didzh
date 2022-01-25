n = [int(x) for x in input() if x.isdigit()]
if len(n) == 10 and n[0] == 9:
    n.insert(0, 8)
    print(f'{n[0]} ({n[1]}{n[2]}{n[3]}) {n[4]}{n[5]}{n[6]}-{n[7]}{n[8]}-{n[9]}{n[10]}')
elif len(n) == 11 and n[1] == 9:
    n[0] = 8
    print(f'{n[0]} ({n[1]}{n[2]}{n[3]}) {n[4]}{n[5]}{n[6]}-{n[7]}{n[8]}-{n[9]}{n[10]}')
else:
    print(''.join(str(x) for x in n))

"""
Другие решения:

num = "".join(filter(str.isdigit, input()))
if len(num) < 10 or len(num) > 11 or num[-10] != '9':
    print(num)
    exit()
phone = "8 (9{}{}) {}{}{}-{}{}-{}{}".format(*num[-9:])
print(phone)


import re
number = "".join(list(filter(lambda x: re.match(r"\d", x), list(input()))))
print(re.sub(r"^(7|8)*(9\d\d)(\d\d\d)(\d\d)(\d\d)$", r"8 (\2) \3-\4-\5", number))
"""