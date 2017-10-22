print('ЗАДАЧА 4 - кирпичный язык')
a=input('Введите слово или фразу: ')
result=''
voc1='а'
voc2='е'
voc3='ё'
voc4='и'
voc5='о'
voc6='у'
voc7='ы'
voc8='э'
voc9='ю'
voc10='я'
for letter in a:
        if (letter == voc1) or(letter == voc2) or(letter == voc3) or (letter == voc4) or (letter == voc5) or (letter == voc6) or(letter == voc7) or (letter == voc8) or (letter == voc9) or (letter == voc10):   
                result += letter + 'с' + letter
        else:
                result += letter 
print('Перевод на кирпичный язык: ', result)
                
            
      
        
        
