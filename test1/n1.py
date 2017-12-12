print('Задание 1-вариант 1')
print()
with open("Extinct_languages.tsv", encoding = "utf -8") as f:
    for line in f:
        if len(line) > 35:
            print(line)
        else:
            pass
