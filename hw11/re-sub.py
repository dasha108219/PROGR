print('Вариант 2\n')

import re

# прилагательных нет

def make_file():
    if fname == '':
        print('Вы не ввели название файла')
        exit(0)
    with open(fname, encoding  = 'utf-8') as file:
        file = file.read()
    return file

def replace(file):
    replace = re.sub(r'В[и́и]кинг[^үстлдв]', r'Бурундук', file)  # чтобы иностранные слова не заменялись,  
    return replace                                              # так как слова типа "Викингтер" (казахский) не формы слова "викинг"

def replace_sec(replace):
    replace_sec= re.sub(r'викинг', r'бурундук', replace)
    return replace_sec

def file_write(replace_sec):   
    with open('replace.txt', 'w', encoding = 'utf-8') as new_file:
        new_file.write(str(replace_sec))
    return new_file

fname = input('Введите название файла, который нужно открыть: ')
file = make_file()
replace = replace(file)
replace_sec = replace_sec(replace)
new_file = file_write(replace_sec)

print('Замена произведена!')
