print('ВАРИАНТ 2')
a=input('Введите слово: ')
for i in range (len (a)):
    for letter in a:
        if( i % 2 == 0) and (letter == a[i]) :  # хотя надо выводит нечетную букву,
                                                # берем четный индекс, т.к. нумерация с 0
            if (letter == 'п') or (letter == 'о') or (letter == 'е'):
                print(letter)
                break
            
        
