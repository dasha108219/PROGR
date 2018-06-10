print('Задание 3\n')

import re

def read_f():
    with open('karenina.xml', encoding = 'utf-8') as f:
        f = f.read()
    return f

def task(f):
    ins = re.findall(r'<w><ana .+ />(\w+)</w>.*\n<w><ana .+ />(\w+)</w>.*\n<w><ana .+ />(\w+)</w>.*\n<w><ana .+ gr="S,.+=твор.*" />(\w+)</w>.*\n<w><ana .+ />(\w+)</w>.*\n<w><ana .+ />(\w+)</w>.*\n<w><ana .+ />(\w+)</w>.*\n', f)
    return ins

def write_f(ins):
    with open('new3.txt', 'w', encoding = 'utf-8') as file:
        for phrase in ins:
            file.write(phrase[0]+' '+phrase[1]+' '+phrase[2]+'\t'+phrase[3]+'\t'+phrase[4]+' '+phrase[5]+' '+phrase[6]+'\n')
    return file


f = read_f()
ins = task(f)
file = write_f(ins)
print('Все в новом файле!')
