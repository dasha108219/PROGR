print('Вариант 2\n')

import re

def read_file(filename):
    with open (filename, encoding = 'utf-8') as file:
        if filename == '':
            exit(0)
        else:
            file = file.read()
    file = file.replace(',', '').replace('\n', '')
    m_sent = '.!?'
    file = file.split('.')
    return file

def sent(file):
    mass = []
    for sentence in file:
        if len(sentence.split()) > 10:
            words = [mass.append(word) for word in sentence.split() if re.match('[А-Я]', word)]
    return mass


filename = input('Введите название файла: ')
file = read_file(filename)
mass = sent(file)

print(mass)
