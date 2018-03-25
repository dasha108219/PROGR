print('Вариант 2\n')

import re

def make_file():
    if fname == '':
        print('Вы не ввели название файла')
        exit(0)
    with open(fname, encoding  = 'utf-8') as file:
        file = file.read()
    return file

def city(file):
    city = re.search(r'<title>(\w+\s*-*\s*\w*) — Википедия</title>', file)
    return city

def time_zone(file):
    time = re.search( r'(UTC[+-−]\d+(?::\d\d)*)</a>(?:, <a .+>(UTC[+-−]\d+(?::\d\d)*)</a></span>)*', file, re.DOTALL)
    if time is None:
        print('Часовой пояс не указан')
        exit(0)
    return time

def file_write(city, time):   
    with open('time_zone.txt', 'a', encoding = 'utf-8') as new_file:
        new_file.write(str(city[1]))
        new_file.write(': ')                                                                                 
        if time[2] is None:                      
            new_file.write(str(time[1]))
        else:
            new_file.write(str(time[1]))
            new_file.write(', летом - ')
            new_file.write(str(time[2]))
        new_file.write('\n')
    return new_file

def to_print(city, time):
    if time[2] is None:
        pr = city[1]+ ': часовой пояс - '+ time[1]
        return pr
    else:
        pr = city[1]+ ': часовой пояс - '+time[1] + ', летом - '+ time[2]
        return pr

fname = input('Введите название файла, который нужно открыть: ')
file = make_file()
city = city(file)
time = time_zone(file)
new_file = file_write(city, time)
pr = to_print(city, time)

print(pr)




