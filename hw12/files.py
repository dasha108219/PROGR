print('Вариант 2\n')

import os

def find_files():
    files = []
    dirpath = '.'
    for filename in os.listdir(dirpath):  
        filepath = os.path.join(dirpath, filename)  
        if os.path.isfile(filepath):
            files.append(filename)
    if files == []:
        print('Файлы не найдены')
        exit(0)
    return files

def without_numb(files):
    mass = []
    for filename in files:
        if ('1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' or '0' ) in filename:
            pass
        else:
            mass.append(filename)
    if mass == []:
        print('Такие файлы не найдены')
        exit(0)
    return mass

def names(mass):
    empty = []
    for filen in mass:
        if filen in empty:
            pass
        else:
            empty.append(filen)
    return empty

files = find_files()
mass = without_numb(files)
empty = names(mass)

print('Найдено файлов без цифр: ', len(mass))
print('Названия всех файлов без цифр: ', empty)





