h = int(input('Введите свой рост, в см: '))
m = int(input('Введите свой вес, в кг: '))
print('')
ind = m / ((h/100) ** 2)
print('Индекс массы тела равен ', round(ind, 2))
print('')
print('Интерпретация показателей ИМТ, результат: ')
if ind <= 16:
    print('Выраженный дефицит массы тела')
elif (ind > 16) and (ind < 18.5):
    print('Недостаточная (дефицит) масса тела')
elif (ind >= 18.5) and (ind <= 24.99):
    print('Норма')
elif (ind >= 25) and (ind < 30):
    print('Избыточная масса тела (предожирение)')
elif (ind >= 30) and (ind < 35):
    print('Ожирение первой степени')
elif (ind >= 35) and (ind < 40):
    print('Ожирение второй степени')
else:
    print('Ожирение третьей степени (морбидное)')

