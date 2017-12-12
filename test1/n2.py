print('Задание 2-вариант 1')
print()
sum_lang = 0
with open("Extinct_languages.tsv", encoding = "utf -8") as f:
    for line in f:
        splitted_line = line.split('\t')
        if splitted_line[2].strip() == 'Critically endangered':
            sum_lang += 1
    print(sum_lang)

