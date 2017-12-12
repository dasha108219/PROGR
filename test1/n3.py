print('Задание 3- вариант 1')
print()
with open("new.txt", 'w', encoding = "utf - 8") as f:
    lang = input()
    while lang != '':
        f.write(lang + "\n")
        lang = input()

with open("Extinct_languages.tsv", encoding = 'utf - 8') as file:
    with open('new.txt',  encoding = 'utf - 8') as f:
        for line in file:
            line = line.strip('\n')
            splitted_line = line.split('\t')
            for lang in f:
                lang = lang.strip()
                if splitted_line[0] == lang:
                    print(splitted_line[0], '-', splitted_line[1], '-', splitted_line[2])
                else:
                    print(lang, '- такого языка нет в списке')
                    
            


    

