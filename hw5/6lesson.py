print('ВАРИАНТ 2')
print()
print('Введите свои слова: ')
with open("new.txt", "w", encoding = "utf - 8") as file:
    word = input()
    while word != "":
        if len(word) > 5:
            file.write("\n") #чтобы new word записывалось с новой строки
            file.write(word)
        word = input()

with open("new.txt", encoding = "utf - 8") as file:
    print(file.read().strip())
