def say_hello():#название функции как переменной
    print('Hello')

say_hello()#вызываю функцию

def plus(a, b):
    print(a+b)

plus(2, 3)
plus('hello', 'world')

def return_sum(a, b):
    s = a + b
    return s

two_plus_three = return_sum(2, 3)
print('2 + 3 =', two_plus_three)


def maximum(a, b):
    if a > b:
        return a
    else:
        return b

def maximum2(a, b):
    if a > b:
        return a
    return b
print(maximum(5, -2))
print(maximum2(-2, 5))

def hello_user(name):
    if len(name) == 0:
        print('Hello anonymus')
        return 
    print('hello ' + name)
hello_user(input('Enter username: '))
