import re #regular expressions

a = re.findall('a', 'abracadabra') #1 - что найти, 2 - строка где найти
print(a) # = abracadabra.count

a = re.findall('a.', 'abracadabra') #1 - что найти, 2 - строка где найти
print(a) # = abracadabra.count / непересекающиеся строки!
# . - любой символ
b = re.findall('[abc].[bd]', 'abracadabra') # сначала а/б/с, вторая - любая, 3 - любой из б/д
print(b)
# [abc]- любой из символов
a = re.findall('[^abc]', 'abracadabra')
print(a)
# ^ - любой символ кроме a/b/c
a = re.findall('[a-z]', 'abracadabra')
print(a)
# все символы между а и зет в таблице символов - все строчные-любой из диапазона
# a-zA-Z0-9 / внутри квадратных скобок точка - любой символ / найти точку - '\.'
a = re.findall('\d', '17.12.2019')
print(int(''.join(a)))
# \d - любая цифра = 0-9
a = re.findall('\D', '17.12.2019')
print(''.join(a))
# налог с большой буквы - все кроме. \D - все кроме цифр
a = re.findall('\d', '17.12.2019')
print(int(''.join(a)))
# \w - буквы и другое = [a-zA-Z0-9_]     \W
# \s - пробел сюда же \n \t    \S - не пробел 
# ^ - символ начала строки (переменной)
# $ - символ конца строки. в конце рв
a = re.findall('^a', 'abracadabra')
print(a)
a = re.findall('\S+') # непробельные после-ти (аналог сплит)
# + (после символа) - символ должен встретится не меньше 1 раза
# _*- >= 0
# _? - 0/1 раз   \w+-?\w*
