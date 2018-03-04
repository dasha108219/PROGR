print('Вариант 2\n')

# формы глагола "найти"

import re

def make_file(fname):
    if fname == '':
        print('Вы не ввели название файла')
        exit(0)
    with open(fname, encoding = 'utf - 8') as file:
        file = file.read()
    file = file.lower()
    symbols = '.,:;!''?-""1234567890'
    for s in symbols:
        file = file.replace(s, '')
    return file

def search_verbs(file):
    all_forms = []
    inf = re.findall('найтиc*[ь]*', file)
                # инфинитив 
    past = re.findall('наш[ле][аило]с*[ья]*', file)
                # прошедшее время
    fut_ger = re.findall('найд[уя]с*[ь]*[штм]*с*[ья]*[ье]*с*[ья]*', file)
                # будущее время и деепричастие (кроме найдешь)
    part_s = re.findall('найдеш*ь*н*[аоу]*[нйю]*[ыао]*[йяегм]*[оу]*', file)
                # стардательные причастия + найдешь
    part_d = re.findall('нашедш[иаеу][йяегмю][оу]*с*я*', file)
                # действительные причастия
    for verb in inf:
        if verb not in all_forms:
            all_forms.append(verb)
    for verb in past:
        if verb not in all_forms:
            all_forms.append(verb)
    for verb in fut_ger:
        if verb not in all_forms:
            all_forms.append(verb)
    for verb in part_s:
        if verb not in all_forms:
            all_forms.append(verb)
    for verb in part_d:
        if verb not in all_forms:
            all_forms.append(verb)
    if all_forms != []:
        print('Найденные формы: ', end = '')
        return all_forms
    else:
        no_verbs = 'Формы глагола "найти" не найдены'
        return no_verbs

fname = input('Введите название файла, который нужно открыть: ')
file = make_file(fname)
all_forms = search_verbs(file)

print(all_forms)
