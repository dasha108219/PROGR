print('ЗАДАЧА 1- среднее арифметическое')
print('Введите числа: ')
a=input()
summa = 0
length = 0
if a == ' ':
    print('Числа не введены, попробуй еще раз')
else:
    a=int(a)
    maximum = a
    minimum =a   
    while a != ' ':
        a = int(a)
        summa += a
        length += 1
        if a > maximum:
            maximum = a
        if a < minimum:
            minimum = a
        a = input()
        if a == ' ':
            break
    print('Среднее арифметическое введенных чисел равно ', summa / length)
    print('Минимальное из введенных чисел равно ', minimum)
    print('Максимальное из введенных чисел равно ', maximum)

    






        
