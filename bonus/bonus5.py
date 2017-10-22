print('ЗАДАЧА 5 - Aigy Paigy')
a=input('Введите слово или фразу: ')
result=''
cons='abcdfghjklmnpqrstvwxyz'
for letter in a:
    if (letter == ' ') or(letter == 'a') or (letter == 'e') or (letter == 'i') or (letter == 'o') or (letter == 'u') or (letter == 'y'):   
        result += letter 
    else:                
        for consonant in cons:
            if letter == consonant:
                result += letter + 'aig'
                break
print('Перевод на Aigy Paigy: ', result)




