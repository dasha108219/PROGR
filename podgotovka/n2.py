print('Задание 2\n')

import re
import collections

def read_f():
    with open('karenina.xml', encoding = 'utf-8') as f:
        f = f.read()
    return f

def task(f):
    keys = re.findall(r'gr="(\w+),' ,f)
    dic = collections.Counter(keys)
    return dic

def write_f(dic):
    with open('new2.txt', 'w', encoding = 'utf-8') as file:
        file.write('Часть речи - Количество\n\n')
        for key, value in dic.items():
            file.write(str(key))
            file.write('\t')
            file.write(str(value))
            file.write('\n')
    return file

f= read_f()
dic = task(f)
file = write_f(dic)
print('Все в новом файле!')

