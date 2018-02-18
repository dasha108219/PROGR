print('Вариант 2', '\n')

# количество точек = количество букв в слове

import random

def make_file(filename):
    d = {}
    with open(filename) as f:
        for line in f:
            adj, noun = line.split(',')
            d[adj] = noun.strip('\n')
    return d

def program_choice(d):
    massiv_for_dots =[]
    keys = list(d.keys())
    choice = random.choice(keys)
    print('Я загадал слово. Попробуйте его угадать')
    print('Подсказка: ', choice, ' ', end = '')
    for i in range(len(d[choice])):
        if i < len(d[choice]):
            print('.', sep ='', end = '')
            i =+ 1
    print('\n')
    return d[choice]

def try_to_guess(choice1):
    win = 'Да, это слово, которое я загадал. Поздравляю, Вы выиграли!'
    empty = 'Вы не ввели слово'
    lose = 'Нет, я загадал другое слово. К сожалению, Вы проиграли'
    a = input('Введите слово: ')
    a = a.lower()
    if a == choice1:
        return win
    elif a == '':
        return empty
    else:
        return lose

filename = 'for-dict.csv'
d = make_file(filename)
choice1 = program_choice(d)
guess = try_to_guess(choice1)

print(guess)
