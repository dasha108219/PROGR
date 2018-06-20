print('Задание 2\n')

import re
import os
import collections

def read_f():
    mass = []
    start_path = "./news/"
    for root, dirs, files in os.walk(start_path):
        for file in files:
            path = start_path + file
            with open(path,encoding = 'utf-8') as f:
                f = f.readlines()
            for line in f:
                words = re.findall('<w><ana lex="([А-Я]\w+)" gr=".+"></ana>', line)
                mass.append(words)
    return mass

def word_freq(mass):
    freq = {}  
    for words in mass:
        for w in words:
           if w in freq:  
               freq[w] += 1 / len(words)
           else:  
               freq[w] = 1 / len(words)
    return freq

def write_f(freq):
    with open('n2.txt', 'w', encoding = 'utf-8') as f:
        f.write('Найденное имя'+'\t'+'Количество вхождений')
        for name, count in freq.items():
            count = int(count)
            f.write(name+ "\t"+ str(count)+ '\n')
    return f
    
    
mass = read_f()
freq = word_freq(mass)
f= write_f(freq)
print('Записан новый файл')

