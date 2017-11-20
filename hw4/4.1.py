print('ВАРИАНТ 2')
print()
with open("new.txt", encoding = "utf -8-sig") as file: #sig- чтобы не было символа начала текста
    lines = file.readlines()
minimum = len(lines[0].replace("\n", "")) #максимальное и минимальные значения изначально равны длине первой строки
maximum = len(lines[0].replace("\n", "")) #убрать символ переноса строки
for line in lines:
    line = line.replace("\n", "")
    if len(line) >= maximum:
        maximum = len(line)
    if len(line) <= minimum and len(line) != 0: #самая короткая строка должна быть непустой
        minimum = len(line)
print('Самая короткая строка меньше самой длинной в', round(maximum / minimum, 3), 'раз(а)')

                          
