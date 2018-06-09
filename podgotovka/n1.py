print('Задание 1\n')

import re

def read_f():
    with open('karenina.xml', encoding = 'utf-8') as f:
        f = f.read()
    return f

def task(f):
    ana = re.findall('<ana ', f)
    word = re.findall('<w>',f)
    aver = len(ana) / len(word)
    return aver

f = read_f()
aver = task(f)
print('Среднее число разборов на слово: ', round(aver, 3))
