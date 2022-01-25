import sys
import re


poem = ''.join(sys.stdin.readlines()).lower()
pmas = re.split(r'[….,():;!?—\s\n\t]', poem.lower()) # Многоточие - отдельный символ!
mas = []
d = dict()
result_list = []
for i in pmas:
    i.strip()
    if len(i) >= 3:
        mas.append(i)
for word in mas:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
sorted_tuple = sorted(d.items(), key=lambda x: (-x[1], x[0]))
print('10 самых часто встречающихся слов в этом тексте:\n')
for i in range(10):
    print(f'{sorted_tuple[i][0]}: {sorted_tuple[i][1]}')



"""
Красиво. Учить регулярки:

import sys 
import re
from collections import Counter

strings = " ".join(sys.stdin.readlines())
words = list(map(str.lower, re.findall(r'\w{3,}', strings)))
result = Counter(sorted(words)).most_common(10)
print("10 самых часто встречающихся слов в этом тексте:\n")
for word in result:
  print(f"{word[0]}: {word[1]}")
"""